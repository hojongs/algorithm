"""
520. Detect Capital
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 'A' <= word[0] <= 'Z':
            cnt = 0
            for c in word:
                if 'A' <= c <= 'Z':
                    cnt += 1
            if cnt == len(word) or cnt == 1:
                return True
            else:
                return False
        else:
            for c in word:
                if 'A' <= c <= 'Z':
                    return False
            return True
