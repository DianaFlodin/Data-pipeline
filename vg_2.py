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
    player_choice = input("Which action do you choose: ")
