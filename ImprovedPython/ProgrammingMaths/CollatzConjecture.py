a = 1

while a != 0:
    a = int(input("Enter intial value: "))
    if a == 0: break
    l = []

    while a != 1:
        l.append(a)
        if a%2 == 0:
            a = a//2
        else:
            a = 3*a + 1
    
    print(l)