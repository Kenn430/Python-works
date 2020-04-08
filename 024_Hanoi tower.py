step = 0

def hanoi(n, A, B, C):
    global step
    if n == 1:
        step += 1
        print(step, A, '-->', C)
    else:
        hanoi(n-1, A, C, B)
        step += 1
        print(step, A, '-->', C)
        hanoi(n-1, B, A, C)

n = int(input('Please give the layers of Hanoi tower: '))
hanoi(n, 'A', 'B', 'C')

