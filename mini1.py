# this is the game where you have to guess the number
import random
print("GUESS THE NUMBER!!!!")
computer=random.randint(1,100)
count=0

while True:

    user=int(input('guess the number:'))
    count=+1
    if(computer==user):
        print(''' congrats!
          you guessed the number''')
        print('attempts taken by you are:',count)
        break
    elif(user>computer):
        print('lower number pleasee')
    else:
        print('higher number please')
    