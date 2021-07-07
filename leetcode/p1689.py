# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
class Solution:
    def minPartitions(self, n: str) -> int:
        m = '1'
        for c in n:
            if c > m:
                m = c

        return int(m)


if __name__ == '__main__':
    print(Solution().minPartitions('32'))
    print(Solution().minPartitions('82734'))
    print(Solution().minPartitions('27346209830709182346'))
