"""Welcome/ Menu Function
Based off 01_Welcome_V3 """

import easygui
def welcome():
    easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")

    user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                    choices=["Add Combo", "Find Combo",
                                             "Delete Combo", "Output Combo",
                                             "Exit"])

    return user_choice


# Main Routine
option = welcome()
print(f"You entered {option}")
