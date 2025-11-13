import os
import gc
import pandas as pd
from tqdm import tqdm
from tabulate import tabulate
from config.source_config import SourceConfig
from matcher import KeywordMatcher
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any, Dict, List, Optional, Set, Tuple, Union
tqdm.pandas()

class EnergyPRMiner:
    def __init__(
        self,
        data_dir: str,
        output_dir: str,
        keyword_rules: List[Union[str, List[Any]]],
        source_configs: List[SourceConfig],
        files_to_search: Optional[List[str]] = None,
        dedupe_rows: bool = False,
        output_format: str = "csv",  # "csv", "json", or "both"
        split_delimiters: Optional[List[str]] = None,
    ):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.matcher = KeywordMatcher(rules=keyword_rules, split_delimiters=split_delimiters)
        self.source_configs = source_configs
        self.files_to_search = files_to_search
        self.dedupe_rows = dedupe_rows
        self.output_format = output_format.lower()
        self.uid = datetime.now(ZoneInfo("America/Winnipeg")).strftime("%m%d-%H-%M")
        os.makedirs(self.output_dir, exist_ok=True)

    # ---------- helpers: load + save ----------

    def _load_source_df(self, cfg: SourceConfig) -> pd.DataFrame:
        file_path = os.path.join(self.data_dir, cfg.filename)

        if cfg.file_type.lower() == "parquet":
            df = pd.read_parquet(file_path)
        elif cfg.file_type.lower() == "csv":
            df = pd.read_csv(file_path)
        else:
            raise ValueError(f"Unsupported file_type='{cfg.file_type}' for {cfg.filename}")

        return df

    def _write_csv(self, df: pd.DataFrame, basename: str) -> str:
        path = os.path.join(self.output_dir, f"{basename}.csv")
        df.to_csv(path, index=False)
        return path

    def _write_json(self, df: pd.DataFrame, basename: str) -> str:
        path = os.path.join(self.output_dir, f"{basename}.json")
        df.to_json(path, orient="records", indent=2, force_ascii=False)
        return path

    def _save_df(self, df: pd.DataFrame, basename: str) -> Dict[str, str]:
        out: Dict[str, str] = {}
        if self.output_format in ("csv", "both"):
            out["csv"] = self._write_csv(df, basename)
        if self.output_format in ("json", "both"):
            out["json"] = self._write_json(df, basename)
        return out

    # ---------- core: process a single source ----------

    def _filter_matches_for_source(self, cfg: SourceConfig) -> Tuple[pd.DataFrame, Set[Any], Dict[str, Any]]:
        # 1. load
        df = self._load_source_df(cfg)

        # 2. debug hints
        missing_cols = [c for c in cfg.cols_to_search if c not in df.columns]
        if missing_cols:
            print(f"[WARN] {cfg.filename}: missing {missing_cols}. Treating them as empty.")
        if cfg.id_col not in df.columns:
            print(f"[WARN] {cfg.filename}: id_col '{cfg.id_col}' not found. Unique ID set may be partial.")

        # 3. define row worker
        #    row_matches(row) -> (did_match, matched_rules_str)
        def _row_worker(row: pd.Series) -> pd.Series:
            did_match, matched_text_str = self.matcher.row_matches_v2(row, cfg.cols_to_search)
            return pd.Series({
                "_matched": did_match,
                "_matched_text": matched_text_str,
            })

        # 4. set up tqdm bar for *this* file
        tqdm.pandas(desc=f"Processing {cfg.filename}", position=1, leave=False)

        # 5. run row-wise apply with progress bar
        match_info = df.progress_apply(_row_worker, axis=1) # type: ignore

        # 6. merge back the match info
        df = pd.concat([df, match_info], axis=1)

        # metadata
        df["_searched_cols"] = ", ".join(cfg.cols_to_search)
        df["_source_file"] = cfg.filename

        del match_info
        gc.collect()

        # 7. filter only matched
        filtered_df = df[df["_matched"]].copy()

        # 8. dedupe if requested
        if self.dedupe_rows and not filtered_df.empty:
            filtered_df = filtered_df.drop_duplicates()

        # 9. collect unique IDs for summary/manifest
        if cfg.id_col in filtered_df.columns:
            unique_ids = set(filtered_df[cfg.id_col].dropna().tolist())
        else:
            unique_ids = set()

        # 10. stats for tabular summary
        stats = {
            "file": cfg.filename,
            "searched_fields": ", ".join(cfg.cols_to_search),
            "rows_matched": len(filtered_df),
            "id_col": cfg.id_col,
        }

        del df
        gc.collect()

        return filtered_df, unique_ids, stats

    # ---------- public API ----------

    def search(self) -> Dict[str, Any]:
        # which configs we're running
        if self.files_to_search:
            configs_to_run = [
                cfg for cfg in self.source_configs
                if cfg.filename in self.files_to_search
            ]
        else:
            configs_to_run = self.source_configs

        all_filtered_frames: List[pd.DataFrame] = []
        summary_rows: List[Dict[str, Any]] = []
        manifest: Dict[str, Any] = {"per_file": {}}

        # outer progress bar (file-level)
        for cfg in tqdm(configs_to_run, desc="Overall progress", unit="file", position=0, leave=True):
            filtered_df, unique_ids, stats = self._filter_matches_for_source(cfg)

            # save this source's matches to CSV/JSON
            paths = self._save_df(filtered_df, cfg.output_name)

            # remember for manifest
            manifest["per_file"][cfg.filename] = {
                "paths": paths,
                "rows_matched": stats["rows_matched"],
                "searched_fields": stats["searched_fields"],
                "unique_ids": list(unique_ids),
            }

            # include in merged
            all_filtered_frames.append(filtered_df)

            # row for final summary table
            summary_rows.append({
                "filename": stats["file"],
                "searched_fields": stats["searched_fields"],
                "total_match": stats["rows_matched"],
            })

        # merge all matched rows across all files
        if all_filtered_frames:
            merged_df = pd.concat(all_filtered_frames, axis=0, ignore_index=True)
        else:
            merged_df = pd.DataFrame()

        merged_paths = self._save_df(merged_df, "all_matches_merged")
        manifest["merged"] = merged_paths

        # build and save summary df
        summary_df = pd.DataFrame(summary_rows)
        summary_paths = self._save_df(summary_df, "summary")
        manifest["summary"] = summary_paths

        # pretty print the summary at the end
        if not summary_df.empty:
            print("\n======================= SUMMARY =======================")
            rows = summary_df.to_dict(orient="records")
            print(tabulate(rows, headers="keys", tablefmt="grid", showindex=False))
        else:
            print("\n===== SUMMARY =====")
            print("No matches found.")
            print("===================\n")
        del merged_df
        gc.collect()
        return manifest