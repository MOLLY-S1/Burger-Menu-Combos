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
text = "Enter the listed combo items"
title = "Combo Enter"
input_list = ["Combo Name", "Burger", "Side", "Drink"]
items = easygui.multenterbox(text, title, input_list)

# User enters item prices
text_price = "Enter Item Price"
title_price = "Combo Price"
input_price = [f"{items[1]}", f"{items[2]}", f"{items[3]}"]
prices = easygui.multenterbox(text_price, title_price, input_price)

# Add the user combo and prices to the dictionary
new_combos[items[0]] = {}
new_combos[items[0]][items[1]] = prices[0]
new_combos[items[0]][items[2]] = prices[1]
new_combos[items[0]][items[3]] = prices[2]

combo = ""
for combo_ID, combo_info in new_combos.items():
    ID = f"\nCombo Name: {combo_ID}"
    for key, value in combo_info.items():
        combo += f"{key}: {value}\n"


easygui.buttonbox(f"Is the following combo correct?\n"
                  f"{ID}\n" f"{combo}", "Combo Check", choices=["Yes", "No"])


