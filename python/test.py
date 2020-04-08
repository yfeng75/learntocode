import random

highest=10
answer=random.randint(1,highest)
print(answer)
print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess !=answer:
    if guess < answer:
       print("Please guess higher")
       guess=int(input())
    else: 
        print('Please guess lower')
        guess=int(input())

print("You got it!")

