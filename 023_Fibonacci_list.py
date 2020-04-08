# Input the position number of a item in Fibonacci sequence, output the value in this position, by list

def fib(position):
    result = [1, 1]
    i = 2
    while i < position:
        result.append(result[i - 1] + result[i - 2])
        i += 1
    return result[position - 1]

position = int(input('Please give the position number: '))
result = fib(position)
print("The number in position %d is %d" % (position, result))

