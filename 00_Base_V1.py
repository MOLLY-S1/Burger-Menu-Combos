import easygui


# Function to welcome user and choose option
def welcome():
    easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")

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
def change(confirm_combo):
    while True:
        combo = ""
        for combo_ID, combo_info in confirm_combo.items():
            ID = f"\nCombo Name: {combo_ID.upper()}"
            for key, value in combo_info.items():
                combo += f"{key}: {value}\n"
        correct = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"{ID}\n" f"{combo}", "Combo Check",
                                    choices=["Yes", "No"])

        if correct == "Yes":
            easygui.msgbox(f"You have sucessfully changed the new combo "
                           f"{combo_ID}", "Combo added")
            return confirm_combo
            break

        change_value = easygui.buttonbox("What would you like to change?",
                                         "Change Choice",
                                         choices=["Item Name",
                                                  "Item Price",
                                                  "Combo Name"])
        if change_value == "Item Name":
            current = blank_check("Enter the current name of the "
                                  "item you wish to change:",
                                  "Current Name")

            while current not in confirm_combo[combo_ID]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an item in this combo:\n\n"
                               f"{ID}\n" f"{combo}", "Error")

                current = blank_check("Enter the current name of the "
                                      "item you wish to change:",
                                      "Current Name")

            new = blank_check(f"Enter the name you want to change"
                              f" {current} to:", "New Name")

            confirm_combo[combo_ID][new] = confirm_combo[combo_ID]. \
                pop(current)


        elif change_value == "Item Price":
            current_price = blank_check("Enter the name of the item "
                                        "which price you wish to "
                                        "change:", "Item Name")
            while current_price not in confirm_combo[combo_ID]:
                easygui.msgbox("Sorry, that is not the name of "
                               "an item in this combo:\n\n"
                               f"{ID}\n" f"{combo}", "Error")

                current_price = blank_check("Enter the name of the "
                                            "item which price you wish "
                                            "to change:", "Item Name", 1, 50)

            new = num_check(f"Enter the price you want to change"
                            f" {current_price} to:", "New price", 1, 50)
            confirm_combo[combo_ID][current_price] = new

        elif change_value == "Combo Name":
            new = blank_check(f"Enter the name you want to change "
                              f"{combo_ID} to:", "New Name").upper()
            confirm_combo[new] = confirm_combo.pop(combo_ID)


# Function to add new combo
def add_combo(combos):
    # Dictionary for new combos to be added and edited from
    new_combos = {}

    # User enters item names
    combo_name = blank_check("Enter Combo Name", "Combo Name").upper()
    burger = blank_check("Enter Burger", "Burger")
    side = blank_check("Enter Side", "Side")
    drink = blank_check("Enter Drink", "Drink")

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

    correct_combo = change(new_combos)

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
        correct_combo = change(searched_combo)

        # Add combo to menu dictionary
        del [combos[search_name]]
        combos.update(correct_combo)

        break

# MAIN ROUTINE

# Combo Menu
combos = {"VALUE":
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
choice = welcome()

while choice != "Exit":
    if choice == "Add Combo":
        add_combo(combos)
        choice = welcome()

    elif choice == "Find Combo":
        find_combo(combos)
        choice = welcome()

    elif choice == "Delete Combo":
        print("Delete Combo")
        choice = welcome()

    elif choice == "Output Combo":
        print("Output Combo")
        choice = welcome()


print("Goodbye")

