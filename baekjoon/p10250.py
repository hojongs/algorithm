testcase = int(input())

for i in range(testcase):
    s = input().split()
    h, w, n = map(int, s)

    temp_n = n
    xx = 1
    while temp_n > h:
        xx += 1
        temp_n -= h
    yy = temp_n

    if xx < 10:
        yyxx = str(yy) + '0' + str(xx)
    else:
        yyxx = str(yy) + str(xx)
    print(yyxx)
