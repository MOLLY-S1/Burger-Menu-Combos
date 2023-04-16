""" Component 5 Blank Checker V2
Use try/accept and pull error messages out of the loop"""
import easygui

error = "Please answer all questions\n"
valid = False

# Continue asking until a valid amount is entered
while not valid:
    try:
        # Ask for input
        enter = easygui.enterbox("Enter:")

        # Check if answer is given
        if enter != "":
            valid = True

        else:
            easygui.msgbox(error)

    except ValueError:
        easygui.msgbox(error)
