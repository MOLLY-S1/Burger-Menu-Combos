"""Final program for Burger-Menu-Combos"""

import easygui
from math import fsum


# Function to welcome user and choose option
def welcome():
    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Combo", "Find Combo",
                                             "Delete Combo", "Output Combo",
                                             "Exit"])

    return user_choice


# Function to check no blanks are entered
def blank_check(question, title):
    error = "That was not a valid input\n" \
            "Please answer all questions"

    while True:
        try:
            response = easygui.enterbox(question, title)
            if response != "":
                return response
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error)


# Function to check floats are entered
def num_check(question, title, low, high):
    error = "That was not a valid input\n" \
            "Please enter a float between {} and {}\n". \
        format(low, high)

    while True:
        try:
            response = float(easygui.enterbox(question, title))
            if low <= response <= high:
                return response
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error)


# Function to change items in combo
def change(confirm_combo, combos):
    while True:
        combo = ""
        for combo_ID, combo_info in confirm_combo.items():
            ID = f"\nCombo Name: {combo_ID.upper()}"
            for key, value in combo_info.items():
                combo += f"{key}: ${value:.2f}\n"
        correct = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"{ID}\n" f"{combo}", "Combo Check",
                                    choices=["Yes", "No"])

        if correct == "Yes":
            easygui.msgbox(f"You have sucessfully changed the new combo "
                           f"{combo_ID}", "Combo added")
            return confirm_combo

        change_value = easygui.buttonbox("What would you like to change?",
                                         "Change Choice",
                                         choices=["Item Name",
                                                  "Item Price",
                                                  "Combo Name"])
        if change_value == "Item Name":
            current = blank_check("Enter the current name of the "
                                  "item you wish to change:",
                                  "Current Name").title()

            while current not in confirm_combo[combo_ID]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an item in this combo:\n\n"
                               f"{ID}\n" f"{combo}", "Error")

                current = blank_check("Enter the current name of the "
                                      "item you wish to change:",
                                      "Current Name").title()

            new = blank_check(f"Enter the name you want to change"
                              f" {current} to:", "New Name").title()

            confirm_combo[combo_ID][new] = confirm_combo[combo_ID]. \
                pop(current)

        elif change_value == "Item Price":
            current_price = blank_check("Enter the name of the item "
                                        "which price you wish to "
                                        "change:", "Item Name").title()
            while current_price not in confirm_combo[combo_ID]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an item in this combo:\n\n"
                               f"{ID}\n" f"{combo}", "Error")

                current_price = blank_check("Enter the name of the "
                                            "item which price you wish "
                                            "to change:", "Item Name").title()

            new = num_check(f"Enter the price you want to change"
                            f" {current_price} to:", "New price", 1, 50)
            confirm_combo[combo_ID][current_price] = new

        elif change_value == "Combo Name":
            new = blank_check(f"Enter the name you want to change "
                              f"{combo_ID} to:", "New Name").upper()
            while new in combos:
                easygui.msgbox(
                    "This name is already in the menu, please choose a "
                    "new name: ", "Error")
                new = blank_check(f"Enter the name you want to change "
                                  f"{combo_ID} to:", "New Name").upper()
            confirm_combo[new] = confirm_combo.pop(combo_ID)


# Function to add new combo
def add_combo(combos):
    # Dictionary for new combos to be added and edited from
    new_combos = {}

    # User enters item names
    combo_name = blank_check("Enter Combo Name", "Combo Name").upper()
    while combo_name in combos:
        easygui.msgbox("This name is already in the menu, please choose a "
                       "new name: ", "Error")
        combo_name = blank_check("Enter Combo Name", "Combo Name").upper()
    burger = blank_check("Enter Burger", "Burger").title()
    side = blank_check("Enter Side", "Side").title()
    drink = blank_check("Enter Drink", "Drink").title()

    # User enters item prices
    burger_price = \
        num_check(f"Enter {burger} Price", "Burger Price", 0.1, 50)
    side_price = num_check(f"Enter {side} Price", "Side Price", 0.1, 50)
    drink_price = num_check(f"Enter {drink} Price", "Drink Price", 0.1, 50)

    # Add the user combo and prices to the dictionary
    new_combos[combo_name] = {}
    new_combos[combo_name][burger] = burger_price
    new_combos[combo_name][side] = side_price
    new_combos[combo_name][drink] = drink_price

    correct_combo = change(new_combos, combos)

    combos.update(correct_combo)


# Function to find combo
def find_combo(combos):
    while True:
        # User enters combo name
        search_name = blank_check("Enter name of combo: ", "Search").upper()

        while search_name not in combos:
            easygui.msgbox(f"Sorry {search_name} is not in the combo menu")

            # User enters combo name
            search_name = blank_check("Enter name of combo: ",
                                      "Search").upper()

        # Add the searched combo to a seperate dictionary
        searched_combo = {search_name: combos[search_name]}

        # Confirm dictionary
        correct_combo = change(searched_combo, combos)

        # Add combo to menu dictionary
        del [combos[search_name]]
        combos.update(correct_combo)

        break


# Function to delete a combo
def delete_combo(combos):
    menu = ""
    # loop to print dictionary
    for comb_ID, combo_info in combos.items():

        # Combo name printed
        menu += f"\n{comb_ID}\n"

        # Loop to print dictionary inside the dictionary
        for key, value in combo_info.items():
            # Combo item and its price printed
            menu += f"{key}: ${value:.2f} \n"
        menu += "--------------------------------"

    # User enters combo name
    choice = blank_check(f"Below is the full combo menu:\n\n"
                         f"{menu}\n\n"
                         f"What would you like to delete:",
                         "Delete Combo").upper()

    while choice not in combos:
        easygui.msgbox(f"Sorry, {choice} is not in the combo menu")

        # User enters combo name
        choice = blank_check(f"Below is the full combo menu:\n\n"
                             f"{menu}\n\n"
                             f"What would you like to delete:",
                             "Delete Combo").upper()

    # Add combo to menu dictionary
    sure = easygui.buttonbox(f"Are you sure you want to delete {choice}\n"
                             f"Once it is deleted this cannot be undone",
                             "Delete Confirm", choices=["Yes", "No"])
    if sure == "Yes":
        del [combos[choice]]
        easygui.msgbox(f"{choice} has been deleted from the menu")


# Function to output combo menu
def output_combo(combos):
    menu = ""

    # loop to print dictionary
    for comb_ID, combo_info in combos.items():

        # Combo name printed
        menu += f"\n{comb_ID}\n"

        # Loop to print dictionary inside the dictionary
        for key, value in combo_info.items():
            # Combo item and its price printed
            menu += f"{key}: ${value:.2f} \n"

        # Prints the total of each combo
        total = fsum(combos[comb_ID].values())
        menu += f"\nTotal: ${total:.2f}\n\n"
        menu += "---------------------------"

    # Output total menu
    easygui.msgbox(f"Total Menu:\n"
                   f"-----------------------\n"
                   f"{menu}\n\n")


# MAIN ROUTINE

# Combo Menu
combo_menu = {"VALUE":
                  {"Beef Burger": 5.69,
                   "Fries": 1.00,
                   "Fizzy Drink": 1.00},
              "CHEEZY":
                  {"Cheeseburger": 6.69,
                   "Fries": 1.00,
                   "Fizzy Drink": 1.00},
              "SUPER":
                  {"Cheeseburger": 6.69,
                   "Large Fries": 2.00,
                   "Smoothie": 2.00}
              }

easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")
choice = welcome()

while choice != "Exit":
    if choice == "Add Combo":
        add_combo(combo_menu)
        choice = welcome()

    elif choice == "Find Combo":
        find_combo(combo_menu)
        choice = welcome()

    elif choice == "Delete Combo":
        delete_combo(combo_menu)
        choice = welcome()

    elif choice == "Output Combo":
        output_combo(combo_menu)
        choice = welcome()

# Print goodbye message
easygui.msgbox("Goodbye!", "Exit")
