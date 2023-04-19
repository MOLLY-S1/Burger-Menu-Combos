import easygui



def change(confirm_combo):
    while True:
        combo = ""
        for combo_ID, combo_info in confirm_combo.items():
            ID = f"\nCombo Name: {combo_ID.upper()}"
            for key, value in combo_info.items():
                combo += f"{key}: {value}\n"
        correct = easygui.buttonbox(f"Is the following combo correct?\n"
                                    f"{ID}\n" f"{combo}", "Combo Check",
                                    choices=["Yes", "No"])


        if correct == "Yes":
            break
        else:
            change_value = easygui.buttonbox("What would you like to change?",
                                             "Change Choice",
                                             choices=["Item Name",
                                                      "Item Price",
                                                      "Combo Name"])
            if change_value == "Item Name":
                current = easygui.enterbox("Enter the current name of the "
                                           "item you wish to change:",
                                           "Current Name")
                while current not in confirm_combo[combo_ID]:
                    easygui.msgbox("Sorry, that is not the name of "
                                   "an item in this combo:\n\n"
                                   f"{ID}\n" f"{combo}", "Error")

                    current = easygui.enterbox("Enter the current name of the "
                                               "item you wish to change:",
                                               "Current Name")

                else:
                    new = easygui.enterbox(f"Enter the name you want to change"
                                           f" {current} to:", "New Name")

                    confirm_combo[combo_ID][new] = confirm_combo[combo_ID].\
                        pop(current)
                    print(confirm_combo[combo_ID])

            if change_value == "Item Price":
                current_price = easygui.enterbox("Enter the name of the item "
                                                 "which price you wish to "
                                                 "change:", "Item Name")
                if current_price not in confirm_combo[combo_ID]:
                    easygui.msgbox("Sorry, that is not the name of "
                                   "an item in this combo:\n\n"
                                   f"{ID}\n" f"{combo}", "Error")

                    current_price = easygui.enterbox("Enter the name of the "
                                                     "item which price you wish "
                                                     "to change:", "Item Name")

                else:
                    new = easygui.enterbox(f"Enter the price you want to change"
                                           f" {current_price} to:", "New price")
                    confirm_combo[combo_ID][current_price] = new

            if change_value == "Combo Name":
                new = easygui.enterbox(f"Enter the name you want to change "
                                       f"{combo_ID} to:", "New Name").upper()
                confirm_combo[new] = confirm_combo.pop(combo_ID)
                print(confirm_combo)

            correct = easygui.buttonbox(f"Is the following combo correct?\n"
                                        f"{ID}\n" f"{combo}", "Combo Check",
                                        choices=["Yes", "No"])


# Main routine
combos = {"VALUE":
          {
              "Beef Burger": 5.69,
              "Fries": 1.00,
              "Fizzy Drink": 1.00}}
change(combos)
print(combos)
