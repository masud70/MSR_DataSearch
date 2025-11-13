from matcher import KeywordMatcher
from constant.keyword import keywords

matcher = KeywordMatcher(rules=keywords, split_delimiters=['.'])

matches = matcher.find_all_matches_in_text("We need to improve energy consumption and battery efficiency.\nOptimizing power usage is crucial for better battery life.")
match = matcher.find_first_match_in_text("We need to improve energy consumption and battery efficiency.\nOptimizing power usage is crucial for better battery life.")

print(match)

for match in matches:
    print(match)