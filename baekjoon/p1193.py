o = int(input())

o2 = 0
t = 1
while o2 < o:
    o2 += t
    t += 1

# print(o2, t)

t -= 1
c = 1
a, b = map(int, '{}/1'.format(t).split('/'))
if t % 2 != 0:
    b, a = a, b
    c = -1

while o2 > o:
    o2 -= 1
    a -= c
    b += c

print('{}/{}'.format(a, b))
