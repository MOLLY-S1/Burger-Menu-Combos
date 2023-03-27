"""Burger Welcome/ Menu Version 3
This code will create a welcome screen and menu, using easygui, the
code from V2 is now in a loop to make testing easier and more efficient"""

import easygui

while True:
    easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")

    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Combo", "Find Combo",
                                             "Delete Combo", "Output Combo",
                                             "Exit"])
    if user_choice == "Add Combo":
        print("Add Combo")

    elif user_choice == "Find Combo":
        print("Find Combo")

    elif user_choice == "Delete Combo":
        print("Delete Combo")

    elif user_choice == "Output Combo":
        print("Output Combo")

    elif user_choice == "Exit":
        print("Goodbye")
        break


