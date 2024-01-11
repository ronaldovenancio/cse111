# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Interest Calculation")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create labels for the number entries and the result.
    lbl_rate = Label(frm_main, text="Rate em % (0 - 100):")
    lbl_period = Label(frm_main, text="Time in years (0 - 40):")
    lbl_amount_of_money = Label(frm_main, text="Amount of money in dollars (0 - 5000000):")
    lbl_payment = Label(frm_main, text="Monthly payment:")

    # Create three number entries.
    ent_rate = FloatEntry(frm_main, width=5, lower_bound=0, upper_bound=100)
    ent_period = IntEntry(frm_main, width=5, lower_bound=0, upper_bound=40)
    ent_amount_of_money = FloatEntry(frm_main, width=8, lower_bound=0, upper_bound=5000000)

    # Create a label to display the result.
    txt_payment = Label(frm_main, width=8, anchor="e")

    # Create labels to display the units.
    lbl_rate_units = Label(frm_main, text="%")
    # Ratios don't have units
    lbl_amount_of_money_units = Label(frm_main, text="dollars")
    lbl_payment_units = Label(frm_main, text="dollars")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, number entries, and buttons in a grid.
    lbl_rate.grid(      row=0, column=0, padx=3, pady=2, sticky="e")
    ent_rate.grid(      row=0, column=1, padx=3, pady=2, sticky="w")
    lbl_rate_units.grid(row=0, column=2, padx=0, pady=2, sticky="w")

    lbl_period.grid(     row=1, column=0, padx=3, pady=2, sticky="e")
    ent_period.grid(     row=1, column=1, padx=3, pady=2, sticky="w")
    # Ratios don't have units.

    lbl_amount_of_money.grid(      row=2, column=0, padx=3, pady=2, sticky="e")
    ent_amount_of_money.grid(      row=2, column=1, padx=3, pady=2, sticky="w")
    lbl_amount_of_money_units.grid(row=2, column=2, padx=0, pady=2, sticky="w")

    lbl_payment.grid(   row=3, column=0, padx=3, pady=2, sticky="e")
    txt_payment.grid(   row=3, column=1, padx=3, pady=2, sticky="w")
    lbl_payment_units.grid(row=3, column=2, padx=0, pady=2, sticky="w")
    btn_clear.grid(    row=3, column=3, padx=3, pady=2)


    # This function is called each time the user releases a key.
    def calculate(event):
        """Compute the approximate payment monthly of a loan."""
        try:
            # Get the user input.
            r = ent_rate.get()
            n = ent_period.get()
            v = ent_amount_of_money.get()

            # Compute the tire payment in dollars.
            p = (v * r/1200 ) / (1 - (1/(1+r/12))**(12 * n))

            # Display the payment rounded to two digits
            # after the decimal for the user to see.
            txt_payment.config(text=f"{p:.2f}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            txt_payment.config(text="")


    # This function is called each time
    # the user clicks the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_rate.clear()
        ent_period.clear()
        ent_amount_of_money.clear()
        txt_payment.config(text="")
        ent_rate.focus()


    # Bind the calculate function to the three number
    # entries so that the calculate function will be called
    # when the user changes the text in the number entries.
    ent_rate.bind("<KeyRelease>", calculate)
    ent_period.bind("<KeyRelease>", calculate)
    ent_amount_of_money.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width text field.
    ent_rate.focus()


# If this file is executed like this:
# > python teach_solution.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
