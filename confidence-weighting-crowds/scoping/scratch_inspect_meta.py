"""Scratch: inspect study-level metadata ONLY (no outcome variables).

This script deliberately does not read the `choice` or `rt` columns. Its purpose
is to confirm the dataset's metadata structure before preregistration.
"""
import pandas as pd

PATH = "data/itc_all_data.csv"
META_COLS = [
    "paper", "subj_idx", "subj_ident", "session", "sess_ident",
    "subj_excl", "subj_excl_ind", "trial_excl", "trial_excl_ind",
    "age", "subset", "subset_label", "country", "currency", "time_unit",
    "procedure", "incentivization", "presentation_of_information",
    "time_pressure", "time_pressure_cont", "online_study",
    "rt_in_full_seconds", "rt_data_analyzed",
    "missing_trials_absolute", "missing_trials_relative",
]

df = pd.read_csv(PATH, usecols=META_COLS, low_memory=False)
print("rows:", len(df))
print("papers:", df["paper"].nunique())
print("subj_ident:", df["subj_ident"].nunique())
print("sess_ident:", df["sess_ident"].nunique())
print("\n--- procedure ---")
print(df["procedure"].value_counts(dropna=False).head(20))
print("\n--- incentivization ---")
print(df["incentivization"].value_counts(dropna=False).head(20))
print("\n--- presentation_of_information ---")
print(df["presentation_of_information"].value_counts(dropna=False).head(20))
print("\n--- time_pressure ---")
print(df["time_pressure"].value_counts(dropna=False).head(10))
print("\n--- online_study ---")
print(df["online_study"].value_counts(dropna=False))
print("\n--- rt_in_full_seconds ---")
print(df["rt_in_full_seconds"].value_counts(dropna=False))
print("\n--- rt_data_analyzed ---")
print(df["rt_data_analyzed"].value_counts(dropna=False))
print("\n--- subj_excl ---")
print(df["subj_excl"].value_counts(dropna=False))
print("\n--- trial_excl ---")
print(df["trial_excl"].value_counts(dropna=False))
print("\n--- rows per paper (desc) ---")
print(df.groupby("paper").size().sort_values(ascending=False).head(10))
print("min rows/paper:", df.groupby("paper").size().min())
print("\n--- time_unit ---")
print(df["time_unit"].value_counts(dropna=False).head(20))
print("--- currency ---")
print(df["currency"].value_counts(dropna=False).head(20))