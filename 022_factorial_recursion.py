# Get the fatorial of a given number by recursion

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

number = int(input('Please give the number for factorial: '))
result = fac(number)
print("Factorial of %d is %d" % (number, result))
