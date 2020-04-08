def fac(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

number = int(input('Please give the number for factorial: '))
result = fac(number)
print("Factorial of %d is %d" % (number, result))
