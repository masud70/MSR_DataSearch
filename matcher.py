import re
import pandas as pd
from typing import Any, Iterable, List, Optional, Tuple, Union

class KeywordMatcher:
    def __init__(self, rules: List[Union[str, List[Any]]], split_delimiters: Optional[List[str]] = None):
        self.rules = rules
        self.split_delimiters = split_delimiters
        
    def split_text(self, text: str) -> List[str]:
        if self.split_delimiters is not None:
            char_class = ''.join(re.escape(d) for d in self.split_delimiters)
            _split_re = re.compile(f'[{char_class}]+')
            parts = _split_re.split(str(text))
            return [p.strip() for p in parts if p and p.strip()]
        else:
            return [text]
            
    def _find_spans_for_pattern(self, text: str, pattern: str) -> Tuple[bool, int, int]:
        match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return True, match.start(), match.end()
        return False, -1, -1

    def _text_matches_pattern(self, text: str, pattern: str) -> Tuple[bool, Optional[str]]:
        matched, start, end = self._find_spans_for_pattern(text, pattern)
        if not matched:
            return False, None
        return True, text[max(0, start-100) : min(len(text), end+100)].strip()

    def _match_rule_list_AND(self, text: str, patterns: List[str]) -> Tuple[bool, Optional[str]]:
        all_matched = []
        for p in patterns:
            matched, matched_text = self._text_matches_pattern(text, p)
            if not matched:
                return False, None
            all_matched.append(matched_text)

        return True, "; ".join(all_matched)

    def _match_rule_two_groups_AND(self, text: str, groupA: List[str], groupB: List[str]) -> Tuple[bool, Optional[str]]:
        hitA = []
        hitB = []
        for p in groupA:
            matched, matched_text = self._text_matches_pattern(text, p)
            if matched:
                hitA.append(matched_text)
                break;
        for p in groupB:
            matched, matched_text = self._text_matches_pattern(text, p)
            if matched:
                hitB.append(matched_text)
                break;

        if not hitA or not hitB:
            return False, None

        return True, "; ".join(hitA + hitB)

    def match_rule(self, text: str, rule: Union[str, List[Any]]) -> Tuple[bool, Optional[str]]:
        if not isinstance(text, str):
            return False

        if isinstance(rule, str):
            # Single token / regex
            return self._text_matches_pattern(text, rule)

        if isinstance(rule, list):
            # Two-group rule?
            if len(rule) == 2 and all(isinstance(g, list) for g in rule):
                return self._match_rule_two_groups_AND(text, rule[0], rule[1])

            # Otherwise AND-rule list
            flat_patterns = [str(x) for x in rule]
            return self._match_rule_list_AND(text, flat_patterns)

        return False, None

    def _rule_label(self, rule: Union[str, List[Any]]) -> str:
        if isinstance(rule, str):
            return rule

        if isinstance(rule, list):
            parts: List[str] = []
            for piece in rule:
                if isinstance(piece, list):
                    parts.extend(str(x) for x in piece)
                else:
                    parts.append(str(piece))
            return " | ".join(parts)

        return str(rule)

    def _split_segments(self, text: str) -> List[str]:
        if not isinstance(text, str):
            return []
        line_chunks = re.split(r"[\r\n]+", text)
        return line_chunks

    def row_matches(
        self,
        row: pd.Series,
        cols_to_search: Iterable[str]
    ) -> Tuple[bool, str]:
        hit_segments: List[str] = []
        for col in cols_to_search:
            flag = False
            if col in row:
                val = row[col]
                for rule in self.rules:
                    matched, matched_text = self.match_rule(str(val), rule)
                    if matched and matched_text is not None:
                        hit_segments.append(matched_text)
                        flag = True
                        break;
            if flag:
                break;
        return len(hit_segments) > 0, " ".join(hit_segments)
    
    def row_matches_v2(
        self,
        row: pd.Series,
        cols_to_search: Iterable[str]
    ) -> Tuple[bool, Optional[str]]:
        for col in cols_to_search:
            if col in row:
                val = row[col]
                text_segments = self.split_text(str(val))
                for segment in text_segments:
                    for rule in self.rules:
                        matched, _ = self.match_rule(segment, rule)
                        if matched:
                            return True, segment
        return False, None
    
    def find_all_matches_in_text(self, text: str) -> List[Tuple[str, str]]:
        matches: List[Tuple[str, str]] = []
        text_segments = self.split_text(text)
        for segment in text_segments:
            for rule in self.rules:
                matched, _ = self.match_rule(segment, rule)
                if matched:
                    matches.append((self._rule_label(rule), segment))
        return matches
    
    def find_first_match_in_text(self, text: str) -> Optional[Tuple[bool, str]]:
        row = pd.Series({"text": text})
        matched, matched_text = self.row_matches_v2(row, ["text"])
        if matched:
            return True, matched_text if matched_text is not None else ""
        return None