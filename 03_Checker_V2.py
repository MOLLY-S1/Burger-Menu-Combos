""" Component 3 Checker V2
Use try/accept and pull error messages out of the loop"""
import easygui

error = "Please enter a float between 1 and 50\n"
valid = False

# Continue asking until a valid amount is entered
while not valid:
     try:
        # Ask for burger price
        price = float(easygui.enterbox("Enter Burger Price:"))

        # Check if amount is within parameters
        if 0 < price <= 10: valid = True

        else:
            easygui.msgbox(error)

     except ValueError:
        easygui.msgbox(error)
