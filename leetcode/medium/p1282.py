"""

"""
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        room = [[] for i in range(500)]
        result = []
        for i in range(len(groupSizes)):
            group_size = groupSizes[i]
            room[group_size].append(i)
            if len(room[group_size]) == group_size:
                result.append(room[group_size])
                room[group_size] = []
        return result


if __name__ == '__main__':
    print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    print(Solution().groupThePeople([2,1,3,3,3,2]))
