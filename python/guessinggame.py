import random

highest=10
answer=random.ranint(1,highest)
print(answer)
print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess !=answer:
    if guess < answer:
       print("Please guess higher")
    else: 
        print ('Please guess lower')

print("You got it the first time")
    

# if guess == answer:
#     print("You got it the first time") 
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer, not equal to.
#         print ('Please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
    

