"""This code uses the chosen trialled code of V2 """

import easygui

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

def num_check(question, title, low, high):
    error = "That was not a valid input\n" \
             "Please enter a float between {} and {}\n".\
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




# Combo menu
combos = {"VALUE":
              {"Beef Burger": 5.69,
               "Fries": 1.00,
               "Fizzy Drink": 1.00},
          "CHEEZY":
              {"Cheeseburger": 6.69,
               "Fries": 1.00,
               "Fizzy Drink":1.00},
          "SUPER":
              {"Cheeseburger": 6.69,
               "Large Fries": 2.00,
               "Smoothie": 2.00}
          }

# Dictionary for new combos to be added and edited from
new_combos = {}


# User enters item names
combo_name = blank_check("Enter Combo Name", "Combo Name").upper()
burger = blank_check("Enter Burger", "Burger")
side = blank_check("Enter Side", "Side")
drink = blank_check("Enter Drink", "Drink")

# User enters item prices
burger_price = \
    num_check(f"Enter {burger} Price", "Burger Price")
side_price = num_check(f"Enter {side} Price", "Side Price")
drink_price = num_check(f"Enter {drink} Price", "Drink Price")

# Add the user combo and prices to the dictionary
new_combos[combo_name] = {}
new_combos[combo_name][burger] = burger_price
new_combos[combo_name][side] = side_price
new_combos[combo_name][drink] = drink_price

combo = ""
for combo_ID, combo_info in new_combos.items():
    ID = f"\nCombo Name: {combo_ID.title()}"
    for key, value in combo_info.items():
        combo += f"{key}: {value}\n"




