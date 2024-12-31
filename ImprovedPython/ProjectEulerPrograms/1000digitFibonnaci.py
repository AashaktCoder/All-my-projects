# Program to find index of the first fibonnaci number with 1000 digits

n1 = 0
n2 = 1

a = 0
n = 1
while len(str(n2)) < 1000:
    a = n2
    n2 = n1 + n2
    n1 = a

    n += 1
print(n2)

print(n)