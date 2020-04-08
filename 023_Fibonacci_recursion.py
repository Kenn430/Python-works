# Imput the position number of a item in Fibonacci sequence, output the value in this position, by recursion

def fib(n):
    if n < 1:
        print('Wrong input!')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

position = int(input('Please give the position number: '))
result = fib(position)
if result != -1:
    print('The number in position %d is %d' % (position, result))
    
