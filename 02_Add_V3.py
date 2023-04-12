"""This code uses the chosen trialled code of V2 """

"""Add Version 1
This Code will store combos in a dictionary"""

import easygui

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
combo_name = easygui.enterbox("Enter Combo Name", "Combo Name")
burger = easygui.enterbox("Enter Burger", "Burger")
side = easygui.enterbox("Enter Side", "Side")
drink = easygui.enterbox("Enter Drink", "Drink")

# User enters item prices
burger_price = easygui.enterbox(f"Enter {burger} Price", "Burger Price")
side_price = easygui.enterbox(f"Enter {side} Price", "Side Price")
drink_price = easygui.enterbox(f"Enter {drink} Price", "Drink Price")

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

easygui.buttonbox(f"Is the following combo correct?\n"
                  f"{ID}\n" f"{combo}", "Combo Check", choices=["Yes", "No"])


