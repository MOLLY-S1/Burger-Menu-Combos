"""Component 7 Version 1, Delete combo"""
import easygui

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

combo = ""
for combo_ID, combo_info in combos.items():
    ID = f"\nCombo Name: {combo_ID.upper()}"
    for key, value in combo_info.items():
        combo += f"{key}: {value}\n"
