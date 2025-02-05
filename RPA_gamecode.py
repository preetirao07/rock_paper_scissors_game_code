# priject:  rock paper scissors
import random
print("Welcome to the RPS Game!")

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))

computers_option = ["Rock", "Paper", "Scissors"]
# computers_choice = print(random.choice(computers_option))

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")


if your_choice==0 and computer_choice ==2:
  print("You win!")
elif computer_choice == 0 and your_choice==2:
  print("You lose!")
elif computer_choice > your_choice:
  print("You lose!")
elif computer_choice == your_choice:
  print("It's a Draw!")
else:
  print("You typed an invalid number. You lose. oops!")