from miner import EnergyPRMiner
from constant.keyword import keywords_v1
from constant.data_source import source_configs

miner = EnergyPRMiner(
    data_dir="./AIDev",
    output_dir="./output/split_by_dot_comma_colon_semi_3x8_keywords",
    split_delimiters=['.', ',', ':', ';'],
    keyword_rules=keywords_v1,
    source_configs=source_configs,
)

manifest = miner.search()