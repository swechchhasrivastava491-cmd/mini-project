#this is the project to build a game of snake, water, gun using python
print('''This is the sanke, water and gun game where you
      have to choose between (snake,water,gun).
      you have three chances to win the game!!
      ALL THE BEST!!!! ''')

import random

# 1 = snake, -1 = water, 0 = gun
choice = ['snake', 'water', 'gun']
computer = random.choice(choice)  # Randomly select for computer
user = input("Choose (snake, water or gun): ").lower()

print(f"Computer chose: {computer}")
print(f"You chose: {user}")

# Determine winner
if user == computer:
    print("It's a draw!")
elif (user == 'snake' and computer == 'water') or \
     (user == 'water' and computer == 'gun') or \
     (user == 'gun' and computer == 'snake'):
    print("You win!")
elif user in choice:
    print("Computer wins!")
else:
    print("Invalid input. Please choose snake, water, or gun.")
