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

menu = ""

# loop to print dictionary
for comb_ID, combo_info in combos.items():

    # Combo name printed
    menu += f"\n{comb_ID}\n"

    # Loop to print dictionary inside the dictionary
    for key, value in combo_info.items():
        # Combo item and its price printed
        menu += f"{key}: ${value} \n"

# User enters combo name
choice = easygui.enterbox(f"Below is the full combo menu:\n\n"
                          f"{menu}\n\n"
                          f"What would you like to delete:", "Delete Combo").upper()

while choice not in combos:
    easygui.msgbox(f"Sorry, {choice} is not in the combo menu")

    # User enters combo name
    choice = easygui.enterbox(f"Below is the full combo menu:\n\n"
                              f"{menu}\n\n"
                              f"What would you like to delete:",
                              "Delete Combo").upper()

# Add combo to menu dictionary
del [combos[choice]]
easygui.msgbox(f"{choice} has been deleted from the menu")

