import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_game = [rock, paper, scissors]
computer_choice = random.choice(rps_game)

player_choice = input("Choose rock, paper or scissors.")

if player_choice=="rock": 
    if computer_choice==rock:
        print(computer_choice+ "Computer's Choice"+ rock+ "Tie")
    elif computer_choice==paper:
        print(computer_choice+ "Computer's Choice"+ rock+ "You Lose")
    elif computer_choice==scissors:
        print(computer_choice+ "Computer's Choice"+ rock+ "You Win")
elif player_choice=="paper":
    if computer_choice==rock:
        print(computer_choice+ "Computer's Choice"+ paper+ "You Win")
    elif computer_choice==scissors:
        print(computer_choice+ "Computer's Choice"+paper+ "You Lose")
    elif computer_choice==paper:
        print(computer_choice+ "Computer's Choice"+paper+ "Tie")
elif player_choice=="scissors":
    if computer_choice==rock:
        print(computer_choice+ "Computer's Choice"+scissors+ "You Lose")
    elif computer_choice==scissors:
        print(computer_choice+ "Computer's Choice"+scissors+ "Tie")
    elif computer_choice==paper:
        print(computer_choice+ "Computer's Choice"+scissors+ "You Win")