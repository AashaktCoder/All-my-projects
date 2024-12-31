def CheckPandigital(n):
    for i in [str(j) for j in range(1, 10)]:
        if not i in str(n): return False
    if len(str(n)) == 9: return True
    else: return False

s = 0
p = []
for i in range(10000):
    for j in range(1000):
        if CheckPandigital(int(str(i) + str(j) + str(i*j))):
            if not (i * j) in p:
                s += i * j
                p.append(i * j)
                print(i, j, i * j)
print(s)