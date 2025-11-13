from analyzer import Analyzer

analyzer = Analyzer(data_dir="./AIDev", output_dir="./output/split_by_comma")
unique_prs_df = analyzer.get_unique_prs()
print(f"Unique PRs DataFrame shape: {unique_prs_df.shape}")