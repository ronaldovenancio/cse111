"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
Purpose: L01 Prove: Milestone.

This program contains the function math.pi and the function round().
Also, I used the while loop.
____________________________________________________________________
"""
#Import math module so I can use math.pi
import math

entrance = "continue"
while entrance != "quite":
     # Print the description of this program for user to see
     print("This program evaluate the volume of space inside a tire")

     # Get the values of the diameter of the wheel in inches, the aspect ratio of the tire and the diameter #of the wheel in inches 
     width_tire = float(input("Enter the width of the wheel in inches (ex 205): "))
     aspect_tire = float(input("Enter the aspect ratio of the tire (ex 60): "))
     diameter_tire = float(input("Enter the diameter of the wheel in inches (ex 15): "))

     # Compute the volume of the tire
     volume_tire = math.pi * (width_tire**2) * aspect_tire * (width_tire * aspect_tire + 2540 * diameter_tire) / 10000000000

     # Print the volume of the tire for the user to see
     volume_tire = round(volume_tire,2)
     print()
     print(f"The approximate volume is {volume_tire} liters.")
     print()
     
     entrance = input("Write QUITE if you wish to exit: ")
     entrance = entrance.lower()





