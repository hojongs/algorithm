# https://www.acmicpc.net/problem/1913
# left top -> N^2
# left -> -1
# left top left -> (N-2)^2


def main():
    n = int(input())
    m = int(input())
    # init table
    table = [[0] * n for _ in range(n)]
    m_pos = None
    # reverse fill loop
    v = pow(n, 2)
    i = 0
    k = 0
    ii = n - 1
    iii = 0
    kk = n - 1
    kkk = 1
    while True:
        # TODO: apply solution https://egg-money.tistory.com/85
        # down
        while True:
            table[i][k] = v
            if v == m:
                m_pos = i, k
            v -= 1
            if i == ii:
                break
            i += 1
        ii -= 1
        k += 1
        if v == 0:
            break
        # right
        while True:
            table[i][k] = v
            if v == m:
                m_pos = i, k
            v -= 1
            if k == kk:
                break
            k += 1
        kk -= 1
        i -= 1
        # up
        while True:
            table[i][k] = v
            if v == m:
                m_pos = i, k
            v -= 1
            if i == iii:
                break
            i -= 1
        iii += 1
        k -= 1
        # left
        while True:
            table[i][k] = v
            if v == m:
                m_pos = i, k
            v -= 1
            if k == kkk:
                break
            k -= 1
        kkk += 1
        i += 1
    print_table(table)
    print(f'{m_pos[0]+1} {m_pos[1]+1}')


def print_table(table):
    for row in table:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == '__main__':
    main()
