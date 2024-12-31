# Program to find highest prime factor of a number

def FindHPF():
    num = int(input("Enter a Number: "))

    hcf = 0

    primeCount = 0

    for i in range(num):

        if i > num//2: break

        if i > 1:
            if num%i == 0:

                for j in range(i):
                    if j > 0 and i%j == 0:
                        primeCount += 1

                if primeCount <= 2:       
                    if i > hcf: hcf = i
                    primeCount = 0

    print(f"The highest prime factor of {num} is {hcf}")
    input("")

FindHPF() 