# https://www.acmicpc.net/problem/1427
def f(num: str) -> str:
    a = []
    b = ''
    for c in num:
        a.append(int(c))

    while True:
        if len(a) == 0:
            return b

        i = 0
        max_i = 0
        while i < len(a):
            if a[i] >= a[max_i]:
                max_i = i
            i += 1
        b += str(a.pop(max_i))


# print(f('2143'))

num = input()
num2 = f(num)
print(num2)
