"""Component 5 Version 1
This Component ensures all boxes are answered"""
import easygui

# User input
enter = easygui.enterbox("Enter here")

while enter == "":
    easygui.msgbox("Please answer all questions")
    enter = easygui.enterbox("Enter here")
