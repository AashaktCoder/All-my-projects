# Program to find numbers solutions to sides of a right triangle for a particular perimeter and doing it for perimeter from 1 to 1000

def FindSides(p):
    n = 0

    for a in range(1, p):
        for b in range(1, p):
            c = (a**2 + b**2)**0.5

            if c.is_integer() and a < b < c:
                if (a + b + int(c)) == p:
                    n += 1
    
    return n

m = 0

for i in range(1, 1001):
    if m < FindSides(i):
        m = FindSides(i)
        print(m, i)

print(m)
