""" Component 3
Ask for user to enter price of burger with parameters
 """

import easygui
# User enters burger price
price = float(easygui.enterbox("Enter Burger Price:"))

# Ask until valid amount is entered
while not 1 <= price <= 50:

    # Show error message
    easygui.msgbox("Please enter a float between 1 and 50")

    # Ask user to enter price again
    price = float(easygui.enterbox("Enter Burger Price:"))

