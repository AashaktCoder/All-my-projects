def CheckPandigital(n):
    for i in [str(j) for j in range(1, 10)]:
        if i not in str(n): return False
    if len(str(n)) == 9: return True
    else: return False

def CheckPrime(n):
    for i in range(2, int(n**0.5)):
        if n%i == 0: return False
    return True

l = []

print(l)