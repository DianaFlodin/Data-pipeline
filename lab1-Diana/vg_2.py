# Du ska skriva "sten sax påse" med hjälp av if-statements och en enklare while-loop.
# Motståndaren är en "computer" som gör helt slumpmässiga val
# Spelaren ska kunna välja 1 av 3 val, dvs. antingen rock, paper eller scissors

# Det räcker med att du kör en runda, du kan förstås lägga till att vinnaren utses efter tex. 3 rundor för att göra det mer realistiskt!
# Känn dig fri att modifiera startkoden, det finns många olika lösningar för detta problem.

import random

game_actions = ["rock", "paper", "scissors"]
continue_game = True

# Vi använder en while-loop för att låta användaren spela igen.
# Du bestämmer själv när spelet ska ta slut genom att använda "break" vilket avbryter while-loopen
while(continue_game):
    # This will choose a random element from the list
    computer_choice = random.choices(game_actions)
    print("0 - Rock, 1 - Paper, 2 - Scissors: ")
    player_choice = input("Which action do you choose (0, 1, 2): ")

# Konvertera spelarens val till motsvarande sträng
    if player_choice == "0":
        player_choice = "rock"
    elif player_choice == "1":
        player_choice = "paper"
    elif player_choice == "2":
        player_choice = "scissors"
    else:
        print("Invalid choice. Please choose 0, 1, or 2.")
        continue

    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")

    # Bestäm vinnaren
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Fråga om spelaren vill spela igen
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        continue_game = False

print("Thanks for playing!")