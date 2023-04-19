"""Component 8 Version 3, output menu, builds on version 2, now a function"""

from math import fsum

import easygui


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

    easygui.msgbox(f"Total Menu:\n"
                   f"-----------------------\n"
                   f"{menu}\n\n")


# MAIN ROUTINE


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
output_combo(combo_menu)
