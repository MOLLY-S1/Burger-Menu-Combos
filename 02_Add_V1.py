"""Add Version 1
This Code will store combos in a dictionary"""

import easygui

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
text = "Enter the listed combo items"
title = "Combo Enter"
input_list = ["Combo Name", "Burger", "Side", "Drink"]
enter = easygui.multenterbox(text, title, input_list)
print(enter)
combos.append(enter)

