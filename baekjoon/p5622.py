s = input()


def parse(c):
    c = c.lower()
    if c in 'abc':
        return 2
    elif c in 'def':
        return 3
    elif c in 'ghi':
        return 4
    elif c in 'jkl':
        return 5
    elif c in 'mno':
        return 6
    elif c in 'pqrs':
        return 7
    elif c in 'tuv':
        return 8
    elif c in 'wxyz':
        return 9


def parse2(n):
    return n + 1


t = 0
for c in s:
    t += parse2(parse(c))

print(t)
