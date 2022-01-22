"""
2114. Maximum Number of Words Found in Sentences
"""
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxN = 0
        for s in sentences:
            maxN = max(maxN, len(s.split()))
        return maxN
