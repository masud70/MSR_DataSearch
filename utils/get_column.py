from typing import Any, List
import pandas as pd
import difflib
from utils import read_file, find_table, get_path
from constant.paths import DATA_DIR

def get_column_values(df: pd.DataFrame, col_name: str) -> List[Any]:
    """
    Return a list of Python-native values from the specified DataFrame column.
    Missing values are converted to None.
    """
    if col_name not in df.columns:
        suggestions = difflib.get_close_matches(col_name, df.columns.tolist(), n=3)
        hint = f" Did you mean: {', '.join(suggestions)}?" if suggestions else ""
        raise KeyError(f"Column '{col_name}' not found in DataFrame.{hint}")

    s = df[col_name].values
    # Convert pandas NA/NaN to None, and coerce to Python-native objects
    # s = s.where(~s.isna(), None).astype(object)
    return [v for v in s.tolist() if v is not pd.NA and (not (isinstance(v, float) and pd.isna(v)))]

def get_mapped_column_values(df: pd.DataFrame, src_col_name: str, src_col_values: List[Any], dest_col_name: str) -> List[Any]:
    """
    Return a list of Python-native values from the specified DataFrame's source column mapped to
    the destination column using the values provided in sor_col_values. Missing values are converted to None.
    """
    if src_col_name not in df.columns:
        suggestions = difflib.get_close_matches(src_col_name, df.columns.tolist(), n=3)
        hint = f" Did you mean: {', '.join(suggestions)}?" if suggestions else ""
        raise KeyError(f"Source column '{src_col_name}' not found in DataFrame.{hint}")
    if dest_col_name not in df.columns:
        suggestions = difflib.get_close_matches(dest_col_name, df.columns.tolist(), n=3)
        hint = f" Did you mean: {', '.join(suggestions)}?" if suggestions else ""
        raise KeyError(f"Destination column '{dest_col_name}' not found in DataFrame.{hint}")

    filtered_df = df[df[src_col_name].isin(src_col_values)]
    s = filtered_df[dest_col_name].values
    return [v for v in s.tolist() if v is not pd.NA and (not (isinstance(v, float) and pd.isna(v)))]

def scr_to_dst_col_value(df: pd.DataFrame, src_file: str, dst_tbl_name: str, src1: str, src2: str, dst: str)->List[Any]:
    masked_df = df.loc[df['_source_file'].eq(src_file)]
    masked_ids = get_column_values(masked_df, src1)
    return get_mapped_column_values(
        read_file(get_path(DATA_DIR, dst_tbl_name), usecols=[src2, dst]),
        src2,
        masked_ids,
        dst
    )