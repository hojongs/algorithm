"""
995. Minimum Number of K Consecutive Bit Flips
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

Time limit exceeded: python의 한계 -> 같은 로직을 TypeScript로 작성하여 성공

Attempt 1:
- flip: A[i] = 1 if A[i] == 0 else 0
- comparison: A[i] == 0
- result: time limit exceeded

Attempt 2:
- flip: A[i] ^= 1 (XOR)
- comparison: A[i] == 0
- result: time limit exceeded

Attempt 3:
- flip: A[i] += 1
- comparison: A[i] % 2 == 0
- result: 가끔씩 success (Runtime: 9720 ms)

Attempt 4:
- flip: for-loop 대신 substitution with map() at single line
- result: 그래도 time limit exceeded

교훈: python에서 time limit exceeded 발생 시 다른 언어(js)로 시도해보자
"""
from typing import List


class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        cnt = 0

        for i in range(len(A)):
            if i + K > len(A):
                if any(map(lambda h: A[h] % 2 == 0, range(i, len(A)))):
                    return -1
                break

            if A[i] % 2 == 0:
                A[i:i+K] = map(lambda v: v + 1, A[i:i+K])
                cnt += 1

        return cnt


if __name__ == '__main__':
    print(Solution().minKBitFlips([0, 1, 0], 1))
    print(Solution().minKBitFlips([1, 1, 0], 2))
    print(Solution().minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
