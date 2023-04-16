import easygui

def change(confirm_combo):
    combo = ""
    for combo_ID, combo_info in confirm_combo.items():
        ID = f"\nCombo Name: {combo_ID.title()}"
        for key, value in combo_info.items():
            combo += f"{key}: {value}\n"
    correct = easygui.buttonbox(f"Is the following combo correct?\n"
              f"{ID}\n" f"{combo}", "Combo Check", choices=["Yes", "No"])

    if correct == "No":
        change_value = easygui.buttonbox("What would you like to change?",
                                         "Change Choice", choices=
                                         ["Item Name", "Item Price",
                                          "Combo Name"])
        if change_value == "Item Name":
            item = easygui.buttonbox("What item do you want to change:",
                                     "Item Name", choices=[[confirm_combo[0][0]],
                                                           [confirm_combo[0][1]],
                                                           [confirm_combo[0][2]]])
            if item in confirm_combo:
                new = easygui.enterbox(f"Enter the name you want to change "
                                       f"{item} to:", "New Name")
                combos.pop(new, item)
                print(combos)

            else:
                easygui.msgbox("Sorry, that is not the name of "
                           "an item in this combo:\n\n"
                           f"{ID}\n" f"{combo}", "Error")
                print(confirm_combo)
# Main routine
combos = {"VALUE":
              {"Beef Burger": 5.69,
               "Fries": 1.00,
               "Fizzy Drink": 1.00}}
change(combos)
