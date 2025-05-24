""" create a program to play Rock, Paper and Scissor Game b/w a computer and a player the program should must be 
readable and understand by end user. """

# I need to take input from user whats he/she choose.
# then I need to take input from computer whats he choose 
# I have to know the rules of game
# now make the logic of the game depend upon the rules 
# now store the score of both players
import time
import random

welcome = "\033[1m🎮Welcome to Rock, Paper And Scissor Game.🎮\033[0m"

print("\t\t\t",welcome)

time.sleep(0.5)
print(
    """Rules of Game:
        Rock  (r)   vs Paper  (p) = Paper  (p)
        Rock  (r)   vs Scissor(s) = Rock   (r)
        Paper (p)   vs Scissor(s) = Scissor(s)
        paper (p)   vs Rock   (r) = paper (p)
        Scissor (s) vs Rock   (r) = Rock (r)
        Scissor (s) vs Paper  (p) = Scissor(s)""")
# 3 variables to store the score
player_score = 0
computer_score = 0
ties = 0
while True: # while loop to reaptedly run the program and ensure user input is correct
    user_choice = input("\nEnter your choice (r/p/s) or 'q' to quit: ")
    if user_choice.lower() == 'q':
        print("Thanks for playing. Bye!🤛")
        break
    elif user_choice not in ["r","p","s"]: #if user_input not in (r/s/p) then print that specified statement 
        print("Invalid Input❌. Please Enter in (r/p/s). Try Again!")
        continue # skip this iteration and continue to execute loop

    options = {'r':"🪨 Rock",'p':"📄 Paper", 's':"✂️ Scissor"} 
    computer_choice = random.choice(['r','s','p']) #random moudle for computer to choose random option

    print(f"User Choice: {options[user_choice]}")
    time.sleep(0.1)
    print(f"Computer Choice: {options[computer_choice]}")

    result = None # result variable is used to store the score
    if user_choice == computer_choice:
        time.sleep(.2)
        print("Tie!🤝")
        result = "tie"
    elif ((user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        time.sleep(.2)
        print("You Won! ")
        result = "User"
    else:
        time.sleep(.2)
        print("Computer Won!💻🏆")
        result = "Computer"

    if result == "User":
        player_score += 1
    elif result == "Computer":
        computer_score += 1
    else:
        ties += 1
time.sleep(.2)
print(f"Player Score: {player_score}")
time.sleep(.1)
print(f"Computer Score 💻: {computer_score}")
time.sleep(.1)
print(f"Ties 🤝: {ties}")

if player_score > computer_score:
    time.sleep(.1)
    print("🎉Congratulation!🎉 You Won.💪🙌")
elif computer_score > player_score:
    time.sleep(.1)
    print("Uh! You Lose.😔")
else:
    time.sleep(.1)
    print("Game Tie🤡")