# Guess a random number between 1 and 10, 3 chances, by wrong guessing get a hint if the guessed number too large or small.

import random
secret = random.randint(1,10)
count = 0
print('------------------------------------------------------------')

while count <= 3:
    if count == 3:
        print('Wrong for too many times!')
        print('Game over!')
        break
    elif count == 0:      
        temp = input('Guess which number is the lucky one: ')      
        guess = int(temp)
    else:    
        temp = input("Sorry but it's wrong, again?: ")     
        guess = int(temp)
 
    if guess == secret:      
        print("Wow, right!")     
        print("But no prize")   
        break
    elif guess < secret:
        print("Too small!")
        count += 1
    else:
        print("Too large!") 
        count += 1

