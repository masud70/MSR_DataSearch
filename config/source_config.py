# config/source_config.py

from dataclasses import dataclass
from typing import List

@dataclass
class SourceConfig:
    filename: str                # e.g. "pr_commits.parquet"
    cols_to_search: List[str]    # e.g. ["message"]
    id_col: str                  # e.g. "pr_id"
    output_name: str             # e.g. "matched_pr_commits"
    file_type: str = "parquet"   # "parquet" or "csv"