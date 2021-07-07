# 1828. Queries on Number of Points Inside a Circle
# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        counts = []
        points2 = dict()
        for i in range(len(points)):
            x, y = points[i]
            points2.setdefault(x, dict())
            points2[x].setdefault(y, 0)

            points2[x][y] += 1

        for query in queries:
            cnt = 0
            rr = pow(query[2], 2)
            for x, v in points2.items():
                for y, c in v.items():
                    if rr >= pow(x - query[0], 2) + pow(y - query[1], 2):
                        cnt += c

            counts.append(cnt)

        return counts


if __name__ == '__main__':
    print(Solution().countPoints(points=[[1, 3], [3, 3], [5, 3], [2, 2]], queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
