from utils import get_path, read_file, get_column_values, get_mapped_column_values, scr_to_dst_col_value
from constant.paths import DATA_DIR, OUTPUT_DIR

merged_path = get_path(OUTPUT_DIR, "all_matches_merged")
dfm = read_file(merged_path)

src_col = "_source_file"
if src_col not in dfm.columns:
        raise KeyError("_source_file column not found.")

pr_ids = []

# Case A1: pr_id present directly in the merged rows
pr_ids.extend(get_column_values(dfm, "pr_id"))

# Case A2: source_file is PR tables -> map via id
pr_ids.extend(get_mapped_column_values(dfm, '_source_file', ["all_pull_request.parquet", "human_pull_request.parquet", "pull_request.parquet"], "id"))

# Case B: source_file is issue -> map via issue
pr_ids.extend(scr_to_dst_col_value(dfm, "issue.parquet", "related_issue.parquet", 'id', "issue_id", "pr_id"))

# Case C: source_file is pr_review_comments -> map via pr_reviews
pr_ids.extend(scr_to_dst_col_value(dfm, "pr_review_comments.parquet", "pr_reviews.parquet", 'pull_request_review_id', "id", "pr_id"))

print(f"Total PR ids found (with duplicates): {len(pr_ids)}")

uniq = set()
for pid in pr_ids:
    if pid is not None:
        try:
            pid_int = int(pid)
            uniq.add(pid_int)
        except ValueError:
            continue

print(f"Total unique PR ids found: {len(uniq)}")
    
df = read_file(
    get_path(DATA_DIR, "all_pull_request.parquet")
)

filtered_df = df[df['id'].isin(uniq)].copy()
filtered_df.to_csv(OUTPUT_DIR / "unique_prs.csv", index=False)
print(f"Written unique PRs to {OUTPUT_DIR / 'unique_prs.csv'}")