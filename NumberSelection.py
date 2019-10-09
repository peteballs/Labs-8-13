import random
computer_numbersTaken = 0
print("Welcome to 'Guess the Number! This is the most unique experience of a lifetime! Please enjoy our creation!")
print("Note: the computer will attempt to guess the number that you select. Let's see if you can outwit the computer and come up with a number that the computer will not be able to guess! Give it your best shot!")
user_number = int(input("Please indicate your secret number (1-10). Do not guess, please put some thought into it. Lol! Please use your best thinking in determining the number and list it here!..........")) 
print("Do not worry, we will not tell the computer! Lol!")
print(f"Your {user_number} is a great selection! Let's see if the computer is smart enough to guess your number! Remember it is a secret!")
while computer_numbersTaken < 500:
  computer_number = random.randint(0,10)
  print(f"The computer selection is ....{computer_number}! ....Let's now compare! The computer is thinking very hard!.....")
  computer_numbersTaken = computer_numbersTaken + 1
  if user_number > computer_number:
    print("Too low! Shame on you computer! Try again if you dare!")
  if user_number < computer_number:
    print("Too high Computer! Shame on you Computer! Try again if you dare!")
  if user_number == computer_number:
    break
if user_number == computer_number:
  #computer_numbersTaken = str(computer_numbersTaken)
  
  print(f"OMG!! It is a miracle!! Your not as dumb as we thought! You diligently determined my number with your amazing forecasting ability in {computer_numbersTaken+1} attempts......Congratulations computer!! You are a true genuius!")
if computer_number != user_number:
    user_number = str(user_number)
    print ("This is incorrect. Unfortunately for the computer, the number chosen was........." + user_number)
    print("Goodbye until we meet again!")