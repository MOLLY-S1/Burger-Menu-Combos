""" Component 5 Blank Checker V3
Now a function
"""
import easygui


def num_check(question):
    error = "That was not a valid input\n" \
             "Please answer all questions"

    while True:
        try:
            response = easygui.enterbox(question)
            if response != "":
                return response
            else:
                easygui.msgbox(error)

        except ValueError:
            easygui.msgbox(error)


# Main Routine
price = num_check("Enter:")
