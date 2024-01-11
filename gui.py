# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    areaofcircle_main_window(frm_main)

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


def areaofcircle_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_radio = Label(frm_main, text="Radio (0 - 1,000,000,000):")

    # Create an integer entry box where the user will enter her age.
    ent_radio = IntEntry(frm_main, width=10, lower_bound=0, upper_bound=1000000000)

    # Create a label that displays "years"
    lbl_rates_units = Label(frm_main, text="unity of lenght")

    # Create a label that displays "Rates:"
    lbl_lenght = Label(frm_main, text="Rates:")

    # Create labels that will display the results.
    lbl_area = Label(frm_main, width=20)
    # lbl_fast = Label(frm_main, width=3)
    lbl_rates_units = Label(frm_main, text="unit of lenght")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radio.grid(      row=0, column=0, padx=3, pady=3)
    ent_radio.grid(      row=0, column=1, padx=3, pady=3)
    lbl_rates_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates_units.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_area.grid(      row=1, column=1, padx=3, pady=3)
   # lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
    lbl_rates_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            radio = ent_radio.get()

            # Compute the user's maximum heart rate.
            # max_rate = 220 - age

            area = math.pi * radio**2

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            # slow = max_rate * 0.65
            # fast = max_rate * 0.85

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            #lbl_slow.config(text=f"{slow:.0f}")
            #lbl_fast.config(text=f"{fast:.0f}")

            lbl_area.config(text=f"{area:.2f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            # lbl_slow.config(text="")
            # lbl_fast.config(text="")

            lbl_area.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        # btn_clear.focus()
        # ent_age.clear()
        # lbl_slow.config(text="")
        # lbl_fast.config(text="")
        # ent_age.focus()

        btn_clear.focus()
        ent_radio.clear()
        lbl_area.config(text="")
        ent_radio.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    # ent_age.bind("<KeyRelease>", calculate)
    ent_radio.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    # ent_age.focus()
    ent_radio.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
