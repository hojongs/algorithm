# Algorithms

## Impressive problems

leetcode/easy/p53.py (DP)

## Leetcode

https://leetcode.com/problemset/all/

[my account](https://leetcode.com/hojongs/)

## Baekjoon Online Judge

https://www.acmicpc.net/problemset

[my account](https://www.acmicpc.net/user/ssaemo)

### Python tips

Python은 기본적으로 느리다. 이로 인한 시간 초과를 피하기 위해, Python보다는 PyPy를 사용하여 제출하기를 권장한다.

백준 사이트는 IO도 코드에서 직접 처리한다 종종 IO 코드가 시간 초과의 원인이 된다

https://www.acmicpc.net/problem/15552

https://www.acmicpc.net/board/view/22716

https://www.acmicpc.net/blog/view/55

https://www.acmicpc.net/blog/view/70

https://wiki.python.org/moin/TimeComplexity

- input
    - sys.stdin.readline() 사용하기 : input() 지양
        - 단, readline()은 \n을 포함하므로, 이를 제외하려면 rstrip()을 함께 사용한다
    - `*` operator를 사용하여 list 초기화하기
      [reference](https://www.geeksforgeeks.org/python-which-is-faster-to-initialize-lists/)
        - 수행 시간 2초 이상에서는 영향이 없었다
    ```python
    import sys

    n = int(sys.stdin.readline())
    strs = [0] * n
    for i in range(n):
        strs[i] = sys.stdin.readline().rstrip()
    ```
- print() 한 번만 호출하기 : print
    - 라고 썼으나, [15552](https://www.acmicpc.net/problem/15552) 에서는 오히려 시간 초과?가 발생했다
    ```python
    output = ''
    for s in strs:
      output += s + '\n'
    print(output)
    ```
- queue 용도로 list 대신 collections.dequeue 사용하기 [reference](https://www.acmicpc.net/blog/view/70)
- Pypy: print()보다 sys.stdout.write() 사용하여 메모리 절약하기 [reference](https://www.acmicpc.net/blog/view/70)
- Pypy는 재귀에 약하다? [reference](https://www.acmicpc.net/blog/view/70)

## Programmers

https://programmers.co.kr/
