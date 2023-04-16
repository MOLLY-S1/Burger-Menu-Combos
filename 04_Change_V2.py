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
                                     "Item Name", choices=[confirm_combo[combo_ID][key],
                                                           confirm_combo[combo_ID][key],
                                                           confirm_combo[combo_ID][key]])
        if change_value == "Item Price":
            price = easygui.buttonbox("What price would you like to change: ",
                                      "Item Price",
                                      choices=[confirm_combo[combo_ID][key],
                                               confirm_combo[combo_ID][key],
                                               confirm_combo[combo_ID][key]])


# Main routine
combos = {"VALUE":
              {"Beef Burger": 5.69,
               "Fries": 1.00,
               "Fizzy Drink": 1.00}}
change(combos)

