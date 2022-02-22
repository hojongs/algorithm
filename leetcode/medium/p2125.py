"""

"""
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        dev_cnt = sum([int(c) for c in bank[0]])
        result = 0
        for i in range(1, len(bank)):
            dev_cnt_2 = sum([int(c) for c in bank[i]])
            if dev_cnt_2 > 0:
                result += dev_cnt * dev_cnt_2
                dev_cnt = dev_cnt_2
        return result


print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]))
print(Solution().numberOfBeams(["000", "111", "000"]))
