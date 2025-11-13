from config.source_config import SourceConfig

source_configs = [
    SourceConfig(
        filename="all_pull_request.parquet",
        cols_to_search=["title", "body"],
        id_col="id",
        output_name="matched_pull_requests",
        file_type="parquet"
    ),
    # SourceConfig(
    #     filename="pull_request.parquet",
    #     cols_to_search=["title", "body"],
    #     id_col="id",
    #     output_name="matched_popular_pull_requests",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_commits.parquet",
    #     cols_to_search=["message"],
    #     id_col="pr_id",
    #     output_name="matched_pr_commits",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_commit_details.parquet",
    #     cols_to_search=["message"],
    #     id_col="pr_id",
    #     output_name="matched_pr_commit_details",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_timeline.parquet",
    #     cols_to_search=["label", "message"],
    #     id_col="pr_id",
    #     output_name="matched_pr_timeline",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_reviews.parquet",
    #     cols_to_search=["body"],
    #     id_col="pr_id",
    #     output_name="matched_pr_reviews",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_review_comments.parquet",
    #     cols_to_search=["diff_hunk", "body"],
    #     id_col="pull_request_review_id",
    #     output_name="matched_pr_review_comments",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_review_comments_v2.parquet",
    #     cols_to_search=["diff_hunk", "body"],
    #     id_col="pull_request_review_id",
    #     output_name="matched_pr_review_comments_v2",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_comments.parquet",
    #     cols_to_search=["body"],
    #     id_col="pr_id",
    #     output_name="matched_pr_comments",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="issue.parquet",
    #     cols_to_search=["title", "body"],
    #     id_col="id",
    #     output_name="matched_issues",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="human_pr_task_type.parquet",
    #     cols_to_search=["title", "reason"],
    #     id_col="id",
    #     output_name="matched_human_pr_task_type",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="human_pull_request.parquet",
    #     cols_to_search=["title", "body"],
    #     id_col="id",
    #     output_name="matched_human_pull_request",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="pr_task_type.parquet",
    #     cols_to_search=["title", "reason"],
    #     id_col="id",
    #     output_name="matched_pr_task_type",
    #     file_type="parquet"
    # ),
    # SourceConfig(
    #     filename="test_data.csv",
    #     cols_to_search=["title", "body"],
    #     id_col="id",
    #     output_name="matched_test_data",
    #     file_type="csv"
    # ),
]