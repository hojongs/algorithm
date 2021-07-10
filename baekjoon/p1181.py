"""
https://www.acmicpc.net/problem/1181

sorting을 python-level에서 구현해서 시간 초과를 경험했다
IO 성능 때문에 시간 초과 경계선을 넘나들기도 했다
"""
import sys
from typing import List


def f(strs: List[str]) -> List[str]:
    strs = sorted(set(strs))
    return sorted(strs, key=len)


n = int(sys.stdin.readline())
strs = [''] * n
for i in range(n):
    strs[i] = sys.stdin.readline().rstrip()

strs2 = f(strs)
out = ''
for str in strs2:
    out += str + '\n'
print(out)

# print(f(['aaa']))
# print(f(['a', 'c', 'b']))
# print(f(['aaa', 'abb', 'baa', 'hefr', 'aaaa']))
# print(f(['c', 'bbb', 'aa']))
# print(f(
#     [
#         'but',
#         'i',
#         'wont',
#         'hesitate',
#         'no',
#         'more',
#         'no',
#         'more',
#         'it',
#         'cannot',
#         'wait',
#         'im',
#         'yours',
#     ]
# ))
