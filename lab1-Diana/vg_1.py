# Skapa ett program som genererar en lista med 100 slumpmässiga nummer.
# Visa en meny för användaren som ger följande val:

# 1. Visa all data i listan (OBS DU SKA INTE BARA PRINTA HELA LISTAN, tex. print(min_lista) är fel)
# 2. Sortera listan stigande
# 3. Sortera listan fallande
# 4. Lägg till ett nummer
# 5. Ta bort ett specifikt nummer
# 6. Ta bort det senaste numret
# 7. Ta bort det första numret
# 8. Summera alla nummer 

# Du ska försöka använda separata funktioner för varje funktionalitet.

# Startkod
import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

def show_data():
    print("All data i listan:")
    for index, number in enumerate(random_numbers):
        print(f"Index {index}: {number}")

def sort_ascending():
    random_numbers.sort()
    print("Listan är sorterad i stigande ordning.")

def sort_descending():
    random_numbers.sort(reverse=True)
    print("Listan är sorterad i fallande ordning.")

def add_number():
    number = int(input("Ange ett nummer att lägga till: "))
    random_numbers.append(number)
    print(f"Numret {number} har lagts till i listan.")

def remove_specific_number():
    number = int(input("Ange ett nummer att ta bort: "))
    if number in random_numbers:
        random_numbers.remove(number)
        print(f"Numret {number} har tagits bort från listan.")
    else:
        print(f"Numret {number} finns inte i listan.")

def remove_last_number():
    if random_numbers:
        removed_number = random_numbers.pop()
        print(f"Det senaste numret {removed_number} har tagits bort från listan.")
    else:
        print("Listan är tom.")

def remove_first_number():
    if random_numbers:
        removed_number = random_numbers.pop(0)
        print(f"Det första numret {removed_number} har tagits bort från listan.")
    else:
        print("Listan är tom.")

def sum_numbers():
    total = sum(random_numbers)
    print(f"Summan av alla nummer i listan är: {total}")

# Logiken för din meny
while True:
    # This prompts to user to enter a choice. It converts it to an integer.
    user_choice = int(input("""
     1. Visa all data i listan
    2. Sortera listan stigande
    3. Sortera listan fallande
    4. Lägg till ett nummer
    5. Ta bort ett specifikt nummer
    6. Ta bort det senaste numret
    7. Ta bort det första numret
    8. Summera alla nummer 
    9. Avsluta
    Välj ett alternativ: """))

    if user_choice == 1:
        show_data()
    elif user_choice == 2:
        sort_ascending()
    elif user_choice == 3:
        sort_descending()
    elif user_choice == 4:
        add_number()
    elif user_choice == 5:
        remove_specific_number()
    elif user_choice == 6:
        remove_last_number()
    elif user_choice == 7:
        remove_first_number()
    elif user_choice == 8:
        sum_numbers()
    elif user_choice == 9:
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val, försök igen.")