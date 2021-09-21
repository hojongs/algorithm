# https://www.acmicpc.net/problem/1914
# info: src, buffer, dst
def hanoi(n, info=(1, 2, 3)):
    if n == 1:
        return [(info[0], info[2])]

    # middle to buffer
    steps = hanoi(n - 1, (info[0], info[2], info[1]))
    # biggest to dst
    steps.append((info[0], info[2]))
    # buffer to dst
    steps += hanoi(n - 1, (info[1], info[0], info[2]))
    return steps


n = int(input())
if n <= 20:
    steps = hanoi(n)
    print(len(steps))
    for step in steps:
        print(step[0], step[1])
else:
    # TODO: need to study
    print(2**n - 1)
