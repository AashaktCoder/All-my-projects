m = 0
s = 0
for a in range(1, 100):
    for b in range(1, 100):
        for i in str(a**b):
            s += int(i)
        if m < s: m = s
        s = 0
print(m)