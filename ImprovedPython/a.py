# for i in range(26): print((chr(65 + i)*(i+1)).lower())

# for i in range(2, 100):
#     for j in range(2, int(i**0.5)+1): 
#         if i%j == 0: break
#     else: print(i)

# print(sum(i**2 for i in range(2, 10, 2)))

# for i in range(1, 100):
#     for j in range(1, i):
#         n = (i**2 + j**2)**0.5
#         if n == int(n): print(i, j, int(n))

# print(sum(1 for i in "hello" if i in "aeiouAEIOU"))

# for i in range(1, 500): print(i) if sum(int(j)**3 for j in str(i)) == i else 0

# n1, n2 = 10, 20
# print(max(i for i in range(1,min(n1,n2)+1) if (n1%i==0 and n2%i==0)))

# print(True) if sorted(list("hello"))==sorted(list("world")) else print(False)

