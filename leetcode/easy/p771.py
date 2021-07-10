# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0

        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    cnt += 1
                    break

        return cnt


if __name__ == '__main__':
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))
