"""
1528. Shuffle String
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shs = [None] * len(s)
        for si, i in enumerate(indices):
            shs[i] = s[si]
        return ''.join(shs)
