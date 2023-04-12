""" Component 3 Checker V4
Now a function
"""
import easygui


def num_check(question, low, high):
    error = "That was not a valid input\n" \
             "Please enter a float between {} and {}\n".\
            format(low, high)

    while True:
        try:
            response = float(easygui.enterbox(question))
            if low <= response <= high:
                return response
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error)


# Main Routine
price = num_check("Enter burger price", 1, 50)
