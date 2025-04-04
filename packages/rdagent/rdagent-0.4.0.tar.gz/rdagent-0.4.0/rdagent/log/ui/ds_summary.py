import math
import re
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from streamlit import session_state as state

from rdagent.log.ui.conf import UI_SETTING


def get_summary_df(log_folders: list[str]) -> tuple[dict, pd.DataFrame]:
    summarys = {}
    for lf in log_folders:
        if not (Path(lf) / "summary.pkl").exists():
            st.warning(
                f"No summary file found in **{lf}**\n\nRun:`dotenv run -- python rdagent/log/mle_summary.py grade_summary --log_folder={lf}`"
            )
        else:
            summarys[lf] = pd.read_pickle(Path(lf) / "summary.pkl")

    if len(summarys) == 0:
        return {}, pd.DataFrame()

    summary = {}
    for lf, s in summarys.items():
        for k, v in s.items():
            stdout_p = Path(lf) / f"{k}.stdout"
            v["stdout"] = []
            if stdout_p.exists():
                # stdout = stdout_p.read_text()
                stdout = ""
                if "Retrying" in stdout:
                    v["stdout"].append("LLM Retry")
                if "Traceback (most recent call last):" in stdout[-10000:]:
                    v["stdout"].append("Code Error")
            v["stdout"] = ", ".join([i for i in v["stdout"] if i])

            # 调整实验名字
            if "amlt" in lf:
                summary[f"{lf[lf.rfind('amlt')+5:].split('/')[0]} - {k}"] = v
            elif "ep" in lf:
                summary[f"{lf[lf.rfind('ep'):]} - {k}"] = v
            else:
                summary[f"{lf} - {k}"] = v

    summary = {k: v for k, v in summary.items() if "competition" in v}
    base_df = pd.DataFrame(
        columns=[
            "Competition",
            "Total Loops",
            "Successful Final Decision",
            "Made Submission",
            "Valid Submission",
            "V/M",
            "Above Median",
            "Bronze",
            "Silver",
            "Gold",
            "Any Medal",
            "Best Medal",
            "SOTA Exp",
            "Ours - Base",
            "Ours vs Base",
            "SOTA Exp Score",
            "Baseline Score",
            "Bronze Threshold",
            "Silver Threshold",
            "Gold Threshold",
            "Medium Threshold",
            "stdout",
        ],
        index=summary.keys(),
    )

    # Read baseline results
    baseline_result_path = UI_SETTING.baseline_result_path
    if Path(baseline_result_path).exists():
        baseline_df = pd.read_csv(baseline_result_path)

    for k, v in summary.items():
        loop_num = v["loop_num"]
        base_df.loc[k, "Competition"] = v["competition"]
        base_df.loc[k, "Total Loops"] = loop_num
        if loop_num == 0:
            base_df.loc[k] = "N/A"
        else:
            base_df.loc[k, "Successful Final Decision"] = v["success_loop_num"]
            base_df.loc[k, "Made Submission"] = v["made_submission_num"]
            base_df.loc[k, "Valid Submission"] = v["valid_submission_num"]
            base_df.loc[k, "Above Median"] = v["above_median_num"]
            base_df.loc[k, "Bronze"] = v["bronze_num"]
            if v["bronze_num"] > 0:
                base_df.loc[k, "Best Medal"] = "bronze"
            base_df.loc[k, "Silver"] = v["silver_num"]
            if v["silver_num"] > 0:
                base_df.loc[k, "Best Medal"] = "silver"
            base_df.loc[k, "Gold"] = v["gold_num"]
            if v["gold_num"] > 0:
                base_df.loc[k, "Best Medal"] = "gold"
            base_df.loc[k, "Any Medal"] = v["get_medal_num"]

            baseline_score = None
            if Path(baseline_result_path).exists():
                baseline_score = baseline_df.loc[baseline_df["competition_id"] == v["competition"], "score"].item()

            base_df.loc[k, "SOTA Exp"] = v.get("sota_exp_stat", None)
            if baseline_score is not None and v.get("sota_exp_score", None) is not None:
                base_df.loc[k, "Ours - Base"] = v["sota_exp_score"] - baseline_score
                try:
                    base_df.loc[k, "Ours vs Base"] = math.exp(
                        abs(math.log(v["sota_exp_score"] / baseline_score))
                    )  # exp^|ln(a/b)|
                except Exception as e:
                    base_df.loc[k, "Ours vs Base"] = None
            base_df.loc[k, "SOTA Exp Score"] = v.get("sota_exp_score", None)
            base_df.loc[k, "Baseline Score"] = baseline_score
            base_df.loc[k, "Bronze Threshold"] = v.get("bronze_threshold", None)
            base_df.loc[k, "Silver Threshold"] = v.get("silver_threshold", None)
            base_df.loc[k, "Gold Threshold"] = v.get("gold_threshold", None)
            base_df.loc[k, "Medium Threshold"] = v.get("median_threshold", None)
            base_df.loc[k, "stdout"] = v["stdout"]

    base_df["SOTA Exp"] = base_df["SOTA Exp"].replace("", pd.NA)
    base_df = base_df.astype(
        {
            "Total Loops": int,
            "Successful Final Decision": int,
            "Made Submission": int,
            "Valid Submission": int,
            "Above Median": int,
            "Bronze": int,
            "Silver": int,
            "Gold": int,
            "Any Medal": int,
            "Ours - Base": float,
            "Ours vs Base": float,
            "SOTA Exp Score": float,
            "Baseline Score": float,
            "Bronze Threshold": float,
            "Silver Threshold": float,
            "Gold Threshold": float,
            "Medium Threshold": float,
        }
    )
    return summary, base_df


def num2percent(num: int, total: int, show_origin=True) -> str:
    if show_origin:
        return f"{num} ({round(num / total * 100, 2)}%)"
    return f"{round(num / total * 100, 2)}%"


def percent_df(df: pd.DataFrame, show_origin=True) -> pd.DataFrame:
    base_df = df.astype("object", copy=True)
    for k in base_df.index:
        loop_num = int(base_df.loc[k, "Total Loops"])
        if loop_num != 0:
            base_df.loc[k, "Successful Final Decision"] = num2percent(
                base_df.loc[k, "Successful Final Decision"], loop_num, show_origin
            )
            if base_df.loc[k, "Made Submission"] != 0:
                base_df.loc[k, "V/M"] = (
                    f"{round(base_df.loc[k, 'Valid Submission'] / base_df.loc[k, 'Made Submission'] * 100, 2)}%"
                )
            else:
                base_df.loc[k, "V/M"] = "N/A"
            base_df.loc[k, "Made Submission"] = num2percent(base_df.loc[k, "Made Submission"], loop_num, show_origin)
            base_df.loc[k, "Valid Submission"] = num2percent(base_df.loc[k, "Valid Submission"], loop_num, show_origin)
            base_df.loc[k, "Above Median"] = num2percent(base_df.loc[k, "Above Median"], loop_num, show_origin)
            base_df.loc[k, "Bronze"] = num2percent(base_df.loc[k, "Bronze"], loop_num, show_origin)
            base_df.loc[k, "Silver"] = num2percent(base_df.loc[k, "Silver"], loop_num, show_origin)
            base_df.loc[k, "Gold"] = num2percent(base_df.loc[k, "Gold"], loop_num, show_origin)
            base_df.loc[k, "Any Medal"] = num2percent(base_df.loc[k, "Any Medal"], loop_num, show_origin)
    return base_df


def days_summarize_win():
    lfs1 = [re.sub(r"log\.srv\d*", "log.srv", folder) for folder in state.log_folders]
    lfs2 = [re.sub(r"log\.srv\d*", "log.srv2", folder) for folder in state.log_folders]
    lfs3 = [re.sub(r"log\.srv\d*", "log.srv3", folder) for folder in state.log_folders]

    _, df1 = get_summary_df(lfs1)
    _, df2 = get_summary_df(lfs2)
    _, df3 = get_summary_df(lfs3)

    df = pd.concat([df1, df2, df3], axis=0)

    def mean_func(x: pd.DataFrame):
        numeric_cols = x.select_dtypes(include=["int", "float"]).mean()
        string_cols = x.select_dtypes(include=["object"]).agg(lambda col: ", ".join(col.fillna("none").astype(str)))
        return pd.concat([numeric_cols, string_cols], axis=0).reindex(x.columns).drop("Competition")

    df = df.groupby("Competition").apply(mean_func)
    if st.toggle("Show Percent", key="show_percent"):
        st.dataframe(percent_df(df, show_origin=False))
    else:
        st.dataframe(df)


def all_summarize_win():
    def shorten_folder_name(folder: str) -> str:
        if "amlt" in folder:
            return folder[folder.rfind("amlt") + 5 :].split("/")[0]
        if "ep" in folder:
            return folder[folder.rfind("ep") :]
        return folder

    selected_folders = st.multiselect(
        "Show these folders", state.log_folders, state.log_folders, format_func=shorten_folder_name
    )
    summary, base_df = get_summary_df(selected_folders)
    if not summary:
        return

    base_df = percent_df(base_df)
    st.dataframe(base_df)
    st.markdown("Ours vs Base: `math.exp(abs(math.log(sota_exp_score / baseline_score)))`")
    st.markdown(f"**统计的比赛数目: :red[{base_df.shape[0]}]**")
    total_stat = (
        base_df[
            [
                "Made Submission",
                "Valid Submission",
                "Above Median",
                "Bronze",
                "Silver",
                "Gold",
                "Any Medal",
            ]
        ]
        != "0 (0.0%)"
    ).sum()
    total_stat.name = "总体统计(%)"
    total_stat.loc["Bronze"] = base_df["Best Medal"].value_counts().get("bronze", 0)
    total_stat.loc["Silver"] = base_df["Best Medal"].value_counts().get("silver", 0)
    total_stat.loc["Gold"] = base_df["Best Medal"].value_counts().get("gold", 0)
    total_stat = total_stat / base_df.shape[0] * 100

    # SOTA Exp 统计
    se_counts = base_df["SOTA Exp"].value_counts(dropna=True)
    se_counts.loc["made_submission"] = se_counts.sum()
    se_counts.loc["Any Medal"] = se_counts.get("gold", 0) + se_counts.get("silver", 0) + se_counts.get("bronze", 0)
    se_counts.loc["above_median"] = se_counts.get("above_median", 0) + se_counts.get("Any Medal", 0)
    se_counts.loc["valid_submission"] = se_counts.get("valid_submission", 0) + se_counts.get("above_median", 0)

    sota_exp_stat = pd.Series(index=total_stat.index, dtype=int, name="SOTA Exp 统计(%)")
    sota_exp_stat.loc["Made Submission"] = se_counts.get("made_submission", 0)
    sota_exp_stat.loc["Valid Submission"] = se_counts.get("valid_submission", 0)
    sota_exp_stat.loc["Above Median"] = se_counts.get("above_median", 0)
    sota_exp_stat.loc["Bronze"] = se_counts.get("bronze", 0)
    sota_exp_stat.loc["Silver"] = se_counts.get("silver", 0)
    sota_exp_stat.loc["Gold"] = se_counts.get("gold", 0)
    sota_exp_stat.loc["Any Medal"] = se_counts.get("Any Medal", 0)
    sota_exp_stat = sota_exp_stat / base_df.shape[0] * 100

    stat_df = pd.concat([total_stat, sota_exp_stat], axis=1)
    stat_t0, stat_t1 = st.columns(2)
    with stat_t0:
        st.dataframe(stat_df.round(2))
        markdown_table = f"""
| xxx | {stat_df.iloc[0,1]:.1f} | {stat_df.iloc[1,1]:.1f} | {stat_df.iloc[2,1]:.1f} | {stat_df.iloc[3,1]:.1f} | {stat_df.iloc[4,1]:.1f} | {stat_df.iloc[5,1]:.1f} | {stat_df.iloc[6,1]:.1f}   |
"""
        st.text(markdown_table)
    with stat_t1:
        Loop_counts = base_df["Total Loops"]
        fig = px.histogram(Loop_counts, nbins=10, title="Total Loops Histogram (nbins=10)")
        mean_value = Loop_counts.mean()
        median_value = Loop_counts.median()
        fig.add_vline(
            x=mean_value, line_color="orange", annotation_text="Mean", annotation_position="top right", line_width=3
        )
        fig.add_vline(
            x=median_value, line_color="red", annotation_text="Median", annotation_position="top right", line_width=3
        )
        st.plotly_chart(fig)

    # write curve
    for k, v in summary.items():
        with st.container(border=True):
            st.markdown(f"**:blue[{k}] - :violet[{v['competition']}]**")
            fc1, fc2 = st.columns(2)
            tscores = {f"loop {k-1}": v for k, v in v["test_scores"].items()}
            tdf = pd.Series(tscores, name="score")
            f2 = px.line(tdf, markers=True, title="Test scores")
            fc2.plotly_chart(f2, key=k)
            try:
                vscores = {k: v.iloc[:, 0] for k, v in v["valid_scores"].items()}

                if len(vscores) > 0:
                    metric_name = list(vscores.values())[0].name
                else:
                    metric_name = "None"

                vdf = pd.DataFrame(vscores)
                vdf.columns = [f"loop {i}" for i in vdf.columns]
                f1 = px.line(vdf.T, markers=True, title=f"Valid scores (metric: {metric_name})")

                fc1.plotly_chart(f1, key=f"{k}_v")
            except Exception as e:
                import traceback

                st.markdown("- Error: " + str(e))
                st.code(traceback.format_exc())
                st.markdown("- Valid Scores: ")
                # st.write({k: type(v) for k, v in v["valid_scores"].items()})
                st.json(v["valid_scores"])


with st.container(border=True):
    if st.toggle("近3天平均", key="show_3days"):
        days_summarize_win()
with st.container(border=True):
    all_summarize_win()
