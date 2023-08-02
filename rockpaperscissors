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

#Write your code below this line 👇
list_of_choices=[rock, paper, scissors]

user_choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n")

user_choice_as_integer=int(user_choice)
print(f"{list_of_choices[user_choice_as_integer]}")    

computer_choice=int(random.randint(0,2))

print(f"Computer chose:\n {list_of_choices[computer_choice]} ")

if user_choice_as_integer==computer_choice:
    print("It is a draw! Press RUN to play again!")

elif computer_choice>user_choice_as_integer or (computer_choice==0 and user_choice_as_integer==2):
    print("You lose!")

elif computer_choice<user_choice_as_integer or (computer_choice==2 and user_choice_as_integer==0):
    print("You win!")

