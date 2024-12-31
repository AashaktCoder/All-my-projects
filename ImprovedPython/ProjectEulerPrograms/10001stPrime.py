primes = []

c = 0
n = 0

i = 0
while n <= 10001:
    i += 1

    for j in range(1, int(i**0.5) + 1):
        if i%j == 0: c += 1

    if c <= 1:
        n += 1
        primes.append(i)

    c = 0

print(primes)