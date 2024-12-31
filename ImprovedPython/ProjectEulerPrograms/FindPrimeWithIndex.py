Primes = []

i = 2
c = 0
while len(Primes) < 10:
    c = 0

    for j in range(1, int(i**0.5) + 1):
        if i%j == 0: 
            c += 1
            if i//j != i and j != 1: c += 1

    if c == 1:
        Primes.append(i)

    i += 1

print(i-1)