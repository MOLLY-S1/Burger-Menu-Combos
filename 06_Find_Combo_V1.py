"""Component 6 Version 1"""
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

# User enters combo name
search_name = easygui.enterbox("Enter name of combo: ", "Search").upper()

if search_name in combos:
    easygui.msgbox(f"{search_name} is a combo in the menu")

else:
    easygui.msgbox(f"Sorry {search_name} is not in the combo menu")
