S = "BANANA"
l = []
v = ['a', 'e', 'i', 'o', 'u']

for i in range(1, len(S)):
    for j in range(len(S)-i+1):
        l.append(S[j:j+i])
l.append(S)

print(len(l))

m = 0
n = 0

for i in l:
    if i[0].lower() in v: m += 1
    else: n += 1

print(m, n)