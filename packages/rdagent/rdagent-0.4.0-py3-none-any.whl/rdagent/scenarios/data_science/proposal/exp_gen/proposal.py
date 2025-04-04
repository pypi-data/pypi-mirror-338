import json
from typing import Dict, List

import pandas as pd

from rdagent.app.data_science.conf import DS_RD_SETTING
from rdagent.components.coder.data_science.ensemble.exp import EnsembleTask
from rdagent.components.coder.data_science.feature.exp import FeatureTask
from rdagent.components.coder.data_science.model.exp import ModelTask
from rdagent.components.coder.data_science.pipeline.exp import PipelineTask
from rdagent.components.coder.data_science.raw_data_loader.exp import DataLoaderTask
from rdagent.components.coder.data_science.workflow.exp import WorkflowTask
from rdagent.core.proposal import ExpGen
from rdagent.oai.llm_utils import APIBackend, md5_hash
from rdagent.scenarios.data_science.experiment.experiment import DSExperiment
from rdagent.scenarios.data_science.proposal.exp_gen.base import DSHypothesis, DSTrace
from rdagent.utils.agent.tpl import T
from rdagent.utils.repo.diff import generate_diff_from_dict
from rdagent.utils.workflow import wait_retry

COMPONENT_TASK_MAPPING = {
    "DataLoadSpec": {
        "target_name": "Data loader and specification generation",
        "spec_file": "spec/data_loader.md",
        "task_output_format": T(".prompts:output_format.data_loader").r(),
        "task_class": DataLoaderTask,
    },
    "FeatureEng": {
        "target_name": "Feature engineering",
        "spec_file": "spec/feature.md",
        "task_output_format": T(".prompts:output_format.feature").r(),
        "task_class": FeatureTask,
    },
    "Model": {
        "target_name": "Model",
        "spec_file": "spec/model.md",
        "task_output_format": T(".prompts:output_format.model").r(),
        "task_class": ModelTask,
    },
    "Ensemble": {
        "target_name": "Ensemble",
        "spec_file": "spec/ensemble.md",
        "task_output_format": T(".prompts:output_format.ensemble").r(),
        "task_class": EnsembleTask,
    },
    "Workflow": {
        "target_name": "Workflow",
        "spec_file": "spec/workflow.md",
        "task_output_format": T(".prompts:output_format.workflow").r(),
        "task_class": WorkflowTask,
    },
    "Pipeline": {
        "target_name": "Pipeline",
        "task_output_format": T(".prompts:output_format.pipeline").r(),
        "task_class": PipelineTask,
    },
}


class DSProposalV1ExpGen(ExpGen):
    def gen(self, trace: DSTrace, max_trace_hist: int) -> DSExperiment:
        # Guidelines:
        # System prompts: Shared condition you are facing
        # - scenario description: `scenario_desc`
        # - expected output format
        # User prompts: Task Specific information
        # - Previous Feedback
        # - Current sota implementation (encourage change based on it)
        # - Extra RAG

        scenario_desc = trace.scen.get_scenario_all_desc()
        sota_exp = trace.sota_experiment()
        assert sota_exp is not None, "SOTA experiment is not provided."
        exp_and_feedback = trace.hist[-1]
        last_exp = exp_and_feedback[0]

        # Step 1: Generate component
        # Describe current best solution using shared template
        sota_exp_desc = T("scenarios.data_science.share:describe.exp").r(
            exp=sota_exp, heading="Best of previous exploration of the scenario"
        )
        last_exp_diff = "\n".join(
            generate_diff_from_dict(sota_exp.experiment_workspace.file_dict, last_exp.experiment_workspace.file_dict)
        )  # we use file_dict for hitting the cache when replicate the experiment in another machine.

        sota_exp_feedback_list = trace.experiment_and_feedback_list_after_init(return_type="sota")
        failed_exp_feedback_list = trace.experiment_and_feedback_list_after_init(return_type="failed")[-max_trace_hist:]
        all_exp_feedback_list = trace.experiment_and_feedback_list_after_init(return_type="all")
        trace_component_to_feedback_df = pd.DataFrame(columns=["component", "hypothesis", "decision"])
        for index, (exp, fb) in enumerate(all_exp_feedback_list):
            trace_component_to_feedback_df.loc[f"trial {index + 1}"] = [
                exp.hypothesis.component,
                exp.hypothesis.hypothesis,
                fb.decision,
            ]

        sota_exp_feedback_list_desc = T("scenarios.data_science.share:describe.trace").r(
            exp_and_feedback_list=sota_exp_feedback_list,
            success=True,
        )
        failed_exp_feedback_list_desc = T("scenarios.data_science.share:describe.trace").r(
            exp_and_feedback_list=failed_exp_feedback_list,
            success=False,
        )

        # Generate component using template with proper context
        component_sys_prompt = T(".prompts:component_gen.system").r(
            scenario=scenario_desc,
            sota_exp_desc=sota_exp_desc,
            last_exp_diff=last_exp_diff,
            component_desc="\n".join(
                [
                    f"[{key}] {value}"
                    for key, value in T("scenarios.data_science.share:component_description").template.items()
                ]
            ),
            component_output_format=T(".prompts:output_format.component").r(),
        )

        component_user_prompt = T(".prompts:component_gen.user").r(
            sota_exp_and_feedback_list_desc=sota_exp_feedback_list_desc,
            failed_exp_and_feedback_list_desc=failed_exp_feedback_list_desc,
            component_and_feedback_df=(
                trace_component_to_feedback_df.to_string()
                if len(trace_component_to_feedback_df) > 0
                else "No experiment and feedback provided"
            ),
        )

        resp_dict_component: dict = json.loads(
            APIBackend().build_messages_and_create_chat_completion(
                component_user_prompt, component_sys_prompt, json_mode=True, json_target_type=Dict[str, str]
            )
        )

        component = resp_dict_component.get("component", "Component not provided")
        component_reason = resp_dict_component.get("reason", "Reason not provided")
        sota_exp_model_file_count = len(
            [
                k
                for k in sota_exp.experiment_workspace.file_dict.keys()
                if k.endswith(".py") and "test" not in k and k.startswith("model")
            ]
        )
        if sota_exp_model_file_count <= 1 and component == "Ensemble":
            component = "Model"

        # Why we should split component selection and steps after?
        # - after we know the selected component, we can use RAG.

        # Step 2: Generate the rest of the hypothesis & task
        component_info = COMPONENT_TASK_MAPPING.get(component)

        if component_info:
            if DS_RD_SETTING.spec_enabled:
                task_spec = sota_exp.experiment_workspace.file_dict[component_info["spec_file"]]
            else:
                task_spec = T(f"scenarios.data_science.share:component_spec.{component}").r()
            system_prompt = T(".prompts:direct_exp_gen.system").r(
                targets=component_info["target_name"],
                component=component,
                scenario=scenario_desc,
                hypothesis_specification=T(".prompts:hypothesis_specification").r(),
                hypothesis_output_format=T(".prompts:output_format.hypothesis").r(),
                task_specification=task_spec,
                task_output_format=component_info["task_output_format"],
                workflow_check=(not component == "Workflow"),
            )

            user_prompt = T(".prompts:direct_exp_gen.user").r(
                targets=component_info["target_name"],
                sota_exp_desc=sota_exp_desc,
                sota_exp_and_feedback_list_desc=sota_exp_feedback_list_desc,
                failed_exp_and_feedback_list_desc=failed_exp_feedback_list_desc,
                last_exp_diff=last_exp_diff,
            )

            def _append_retry(args: tuple, kwargs: dict) -> tuple[tuple, dict]:
                # Only modify the user_prompt on retries (i > 0)
                user_prompt = args[0]
                user_prompt += "\n\nretrying..."
                return (user_prompt,), kwargs

            @wait_retry(retry_n=5, transform_args_fn=_append_retry)
            def _f(user_prompt):
                resp_dict = json.loads(
                    APIBackend().build_messages_and_create_chat_completion(
                        user_prompt=user_prompt,
                        system_prompt=system_prompt,
                        json_mode=True,
                        # NOTE: corner cases.
                        # workflow_update may be a string
                        # model could have 2 level nested dict.
                        json_target_type=dict[str, dict[str, str | dict] | str],
                    )
                )
                assert "hypothesis_proposal" in resp_dict, "Hypothesis proposal not provided."
                assert "task_design" in resp_dict, "Task design not provided."
                task_class = component_info["task_class"]
                hypothesis_proposal = resp_dict.get("hypothesis_proposal", {})
                hypothesis = DSHypothesis(
                    component=component,
                    hypothesis=hypothesis_proposal.get("hypothesis", ""),
                    reason=component_reason + "\n" + hypothesis_proposal.get("reason", ""),
                    concise_reason=hypothesis_proposal.get("concise_reason", ""),
                    concise_observation=hypothesis_proposal.get("concise_observation", ""),
                    concise_justification=hypothesis_proposal.get("concise_justification", ""),
                    concise_knowledge=hypothesis_proposal.get("concise_knowledge", ""),
                )

                task_design = resp_dict.get("task_design", {})
                task_name = task_design["model_name"] if component == "Model" else component
                description = task_design.get(
                    "description", f"{component_info['target_name']} description not provided"
                )
                task = task_class(
                    name=task_name,
                    description=description,
                    **{k: task_design.get(k, v) for k, v in component_info.get("extra_params", {}).items()},
                )
                new_workflow_desc = resp_dict.get("workflow_update", "No update needed")
                return hypothesis, task, new_workflow_desc

            hypothesis, task, new_workflow_desc = _f(user_prompt)

            exp = DSExperiment(pending_tasks_list=[[task]], hypothesis=hypothesis)
            # exp.experiment_workspace.inject_code_from_folder(sota_exp.experiment_workspace.workspace_path)
            exp.experiment_workspace.inject_code_from_file_dict(sota_exp.experiment_workspace)

            if new_workflow_desc != "No update needed":
                workflow_task = WorkflowTask(
                    name="Workflow",
                    description=new_workflow_desc,
                )
                exp.pending_tasks_list.append([workflow_task])
            return exp
        else:
            raise ValueError(f"Unknown component: {component}")


class DSProposalV2ExpGen(ExpGen):
    def identify_scenario_problem(self, scenario_desc: str, competition_desc: str, sota_exp_desc: str) -> Dict:
        sys_prompt = T(".prompts_v2:scenario_problem.system").r(
            problem_spec=T(".prompts_v2:specification.problem").r(),
            problem_output_format=T(".prompts_v2:output_format.problem").r(),
        )
        user_prompt = T(".prompts_v2:scenario_problem.user").r(
            scenario_desc=scenario_desc,
            competition_desc=competition_desc,
            sota_exp_desc=sota_exp_desc,
        )
        response = APIBackend().build_messages_and_create_chat_completion(
            user_prompt=user_prompt,
            system_prompt=sys_prompt,
            json_mode=True,
            json_target_type=Dict[str, Dict[str, str]],
        )
        return json.loads(response)

    def identify_feedback_problem(
        self,
        scenario_desc: str,
        sota_exp_feedback_list_desc: str,
        failed_exp_feedback_list_desc: str,
        sota_exp_desc: str,
        pipeline: bool,
    ) -> Dict:
        sys_prompt = T(".prompts_v2:scenario_problem.system").r(
            problem_spec=T(".prompts_v2:specification.problem").r(),
            problem_output_format=T(".prompts_v2:output_format.problem").r(),
        )
        user_prompt = T(".prompts_v2:feedback_problem.user").r(
            scenario_desc=scenario_desc,
            sota_exp_and_feedback_list_desc=sota_exp_feedback_list_desc,
            failed_exp_and_feedback_list_desc=failed_exp_feedback_list_desc,
            sota_exp_desc=sota_exp_desc,
        )
        response = APIBackend().build_messages_and_create_chat_completion(
            user_prompt=user_prompt,
            system_prompt=sys_prompt,
            json_mode=True,
            json_target_type=Dict[str, Dict[str, str]],
        )
        return json.loads(response)

    def hypothesis_gen(
        self,
        component_desc: str,
        scenario_desc: str,
        sota_exp_feedback_list_desc: str,
        failed_exp_feedback_list_desc: str,
        sota_exp_desc: str,
        problems: list,
        pipeline: bool,
    ) -> Dict:
        sys_prompt = T(".prompts_v2:hypothesis_gen.system").r(
            component_desc=component_desc,
            hypothesis_spec=T(".prompts_v2:specification.hypothesis").r(),
            hypothesis_output_format=T(".prompts_v2:output_format.hypothesis").r(pipeline=pipeline),
            pipeline=pipeline,
        )
        user_prompt = T(".prompts_v2:hypothesis_gen.user").r(
            scenario_desc=scenario_desc,
            sota_exp_and_feedback_list_desc=sota_exp_feedback_list_desc,
            failed_exp_and_feedback_list_desc=failed_exp_feedback_list_desc,
            sota_exp_desc=sota_exp_desc,
            problems=json.dumps(problems, indent=2),
        )
        response = APIBackend().build_messages_and_create_chat_completion(
            user_prompt=user_prompt,
            system_prompt=sys_prompt,
            json_mode=True,
            json_target_type=Dict[str, Dict[str, str | Dict[str, str | int]]],
        )
        return json.loads(response)

    def hypothesis_rank(self, hypothesis_dict: dict, problem_dict: dict, pipeline: bool) -> DSHypothesis:
        # TODO use rule base or llm to rank the hypothesis
        if pipeline:
            problem_dict = {k: v for k, v in hypothesis_dict.items() if v.get("component", "") == "Pipeline"}

        weights = {
            "alignment_score": 0.2,
            "impact_score": 0.4,
            "novelty_score": 0.2,
            "feasibility_score": 0.1,
            "risk_reward_balance_score": 0.1,
        }
        scores_dict = {}
        for problem_name in hypothesis_dict:
            scores_dict[problem_name] = {}
            for score_key in weights:
                if score_key not in hypothesis_dict[problem_name]["evaluation"]:
                    scores_dict[problem_name][score_key] = 0
                else:
                    try:
                        scores_dict[problem_name][score_key] = (
                            float(hypothesis_dict[problem_name]["evaluation"][score_key]) * weights[score_key]
                        )
                    except (ValueError, TypeError):
                        scores_dict[problem_name][score_key] = 0
        scores = pd.DataFrame(scores_dict)
        scores_sorted = scores.sum().sort_values(ascending=False)
        if len(scores_sorted) > 5:
            scores_sorted = scores_sorted[: len(scores_sorted) // 2]

        reproducible_int = int.from_bytes(bytes.fromhex(md5_hash(scores_sorted.to_string())), byteorder="big") % len(
            scores_sorted
        )
        max_score_problem_name = scores_sorted.index[reproducible_int]
        problem = problem_dict.get(max_score_problem_name, {}).get("problem", "Problem not provided")

        return DSHypothesis(
            component=hypothesis_dict[max_score_problem_name]["component"],
            hypothesis=hypothesis_dict[max_score_problem_name]["hypothesis"],
            reason=hypothesis_dict[max_score_problem_name]["reason"],
            problem=problem,
        )

    def task_gen(
        self,
        component_desc: str,
        scenario_desc: str,
        sota_exp_desc: str,
        sota_exp: DSExperiment,
        hypothesis: DSHypothesis,
        pipeline: bool,
    ) -> DSExperiment:
        component_info = COMPONENT_TASK_MAPPING.get(hypothesis.component)
        if not pipeline and DS_RD_SETTING.spec_enabled and sota_exp is not None:
            task_spec = sota_exp.experiment_workspace.file_dict[component_info["spec_file"]]
        else:
            task_spec = T(f"scenarios.data_science.share:component_spec.{hypothesis.component}").r()
        sys_prompt = T(".prompts_v2:task_gen.system").r(
            targets=component_info["target_name"],
            task_specification=task_spec,
            task_output_format=component_info["task_output_format"],
            component_desc=component_desc,
            workflow_check=not pipeline and hypothesis.component != "Workflow",
        )
        user_prompt = T(".prompts_v2:task_gen.user").r(
            scenario_desc=scenario_desc, sota_exp_desc=sota_exp_desc, hypothesis=str(hypothesis)
        )
        response = APIBackend().build_messages_and_create_chat_completion(
            user_prompt=user_prompt,
            system_prompt=sys_prompt,
            json_mode=True,
            json_target_type=Dict[str, str | Dict[str, str]],
        )
        task_dict = json.loads(response)
        task_design = task_dict.get("task_design", {})
        task_name = task_design["model_name"] if hypothesis.component == "Model" else hypothesis.component
        description = (
            task_design
            if isinstance(task_design, str)
            else task_design.get("description", f"{component_info['target_name']} description not provided")
        )
        task_class = component_info["task_class"]
        task = task_class(
            name=task_name,
            description=description,
        )
        new_workflow_desc = task_dict.get("workflow_update", "No update needed")
        exp = DSExperiment(pending_tasks_list=[[task]], hypothesis=hypothesis)
        # exp.experiment_workspace.inject_code_from_folder(sota_exp.experiment_workspace.workspace_path)
        if sota_exp is not None:
            exp.experiment_workspace.inject_code_from_file_dict(sota_exp.experiment_workspace)

        if not pipeline and new_workflow_desc != "No update needed":
            workflow_task = WorkflowTask(
                name="Workflow",
                description=new_workflow_desc,
            )
            exp.pending_tasks_list.append([workflow_task])
        return exp

    def gen(self, trace: DSTrace, max_trace_hist: int, pipeline: bool = False) -> DSExperiment:
        component_desc = "\n".join(
            [
                f"[{key}] {value}"
                for key, value in T("scenarios.data_science.share:component_description").template.items()
            ]
        )

        sota_exp = trace.sota_experiment()
        scenario_desc = trace.scen.get_scenario_all_desc()
        competition_desc = trace.scen.get_competition_full_desc()

        sota_exp_desc = T("scenarios.data_science.share:describe.exp").r(
            exp=sota_exp, heading="Best of previous exploration of the scenario"
        )

        sota_exp_feedback_list = trace.experiment_and_feedback_list_after_init(return_type="sota")
        failed_exp_feedback_list = trace.experiment_and_feedback_list_after_init(return_type="failed")[-max_trace_hist:]

        sota_exp_feedback_list_desc = T("scenarios.data_science.share:describe.trace").r(
            exp_and_feedback_list=sota_exp_feedback_list,
            success=True,
        )
        failed_exp_feedback_list_desc = T("scenarios.data_science.share:describe.trace").r(
            exp_and_feedback_list=failed_exp_feedback_list,
            success=False,
        )

        # Step 1: Identify problems
        scen_problems = self.identify_scenario_problem(
            scenario_desc=scenario_desc,
            competition_desc=competition_desc,
            sota_exp_desc=sota_exp_desc,
        )
        fb_problems = self.identify_feedback_problem(
            scenario_desc=scenario_desc,
            sota_exp_feedback_list_desc=sota_exp_feedback_list_desc,
            failed_exp_feedback_list_desc=failed_exp_feedback_list_desc,
            sota_exp_desc=sota_exp_desc,
            pipeline=pipeline,
        )
        all_problems = {**scen_problems, **fb_problems}

        # Step 2: Propose hypothesis based on the identified problems
        hypothesis_dict = self.hypothesis_gen(
            component_desc=component_desc,
            scenario_desc=scenario_desc,
            sota_exp_feedback_list_desc=sota_exp_feedback_list_desc,
            failed_exp_feedback_list_desc=failed_exp_feedback_list_desc,
            sota_exp_desc=sota_exp_desc,
            problems=all_problems,
            pipeline=pipeline,
        )
        if not pipeline:
            sota_exp_model_file_count = len(
                [
                    k
                    for k in sota_exp.experiment_workspace.file_dict.keys()
                    if k.endswith(".py") and "test" not in k and k.startswith("model")
                ]
            )
            if sota_exp_model_file_count <= 1:
                pop_names = []
                for problem_name in hypothesis_dict:
                    if hypothesis_dict[problem_name].get("component", "") == "Ensemble":
                        pop_names.append(problem_name)
                for name in pop_names:
                    hypothesis_dict.pop(name)

        # Step 3: Select the best hypothesis
        new_hypothesis = self.hypothesis_rank(
            hypothesis_dict=hypothesis_dict,
            problem_dict=all_problems,
            pipeline=pipeline,
        )

        return self.task_gen(
            component_desc=component_desc,
            scenario_desc=scenario_desc,
            sota_exp_desc=sota_exp_desc,
            sota_exp=sota_exp,
            hypothesis=new_hypothesis,
            pipeline=pipeline,
        )
