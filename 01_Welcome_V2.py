"""Version 2
This code will create a welcome screen and menu, using easygui"""
import easygui

easygui.msgbox("Welcome to Burger Menu Combos", "Welcome")

user_choice = easygui.buttonbox("Please choose an option:", "Menu Options",
                                choices=["Add Combo", "Find Combo",
                                         "Delete Combo", "Output Combo",
                                         "Exit"])
if user_choice == "Add Combo":
    easygui.msgbox("Add Combo")

elif user_choice == "Find Combo":
    easygui.msgbox("Find Combo")

elif user_choice == "Delete Combo":
    easygui.msgbox("Delete Combo")

elif user_choice == "Output Combo":
    easygui.msgbox("Output Combo")

elif user_choice == "Exit":
    easygui.msgbox("Exit")


