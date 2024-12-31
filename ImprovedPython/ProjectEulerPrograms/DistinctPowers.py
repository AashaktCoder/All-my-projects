def FindDistinctPowers(a, b):
    Lis = []
    for i in range(2, a+1):
        for j in range(2, b+1):
            if not ((i**j) in Lis):
                Lis.append(i**j)
    
    return len(Lis)

print(FindDistinctPowers(100, 100))
