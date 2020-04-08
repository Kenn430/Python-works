def fib(n):
    n1 = 1
    n2 = 1
    n3 = 1
    
    if n < 1:
        print('Wrong input!')
        return -1

    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1

    return(n3)


position = int(input('Please give the position number: '))
result = fib(position)

if result != -1:
    print('The number in position %d is %d' % (position, result))
