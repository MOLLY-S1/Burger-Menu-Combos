"""Component 8 Version 1, output menu"""

import easygui

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

menu = ""

# loop to print dictionary
for comb_ID, combo_info in combo_menu.items():

    # Combo name printed
    menu += f"\n{comb_ID}\n"

    # Loop to print dictionary inside the dictionary
    for key, value in combo_info.items():
        # Combo item and its price printed
        menu += f"{key}: ${value} \n"

easygui.msgbox(f"Total Menu:\n\n"
               f"{menu}\n\n")
