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
        easygui.msgbox("Oh no, please re-enter the combo information")

combos = {"VALUE":
              {"Beef Burger": 5.69,
               "Fries": 1.00,
               "Fizzy Drink": 1.00}}
change(combos)

