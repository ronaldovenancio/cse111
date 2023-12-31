"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
Purpose: L02 Prove: Milestone.

This program contains the function math.pi and the function round().
Also, I used the while loop.

This program  prints the tire volume to the terminal window and it asks the user if she wants to buy tires with the dimensions that she entered. If the user answers “yes”, it program asks for her/his phone number and store her/his phone number in the volumes.txt file.
____________________________________________________________________
"""
#Import math module so I can use math.pi
import math
from datetime import datetime

today = datetime.now()
print(today)

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

     print("Do you want to buy tires with these dimensions? ")
     answer = input("Write YES if you wish to buy them or NOT: ")
     answer = answer.lower()

     if answer == "yes":
          phone = input("What is your phone number? ")
          with open("volumes.txt", "at") as volumes_file:
              print(file=volumes_file)
              print(f" {today}, {width_tire}, {aspect_tire}, {volume_tire}, {phone}",file=volumes_file)
     if answer != "yes":   
         with open("volumes.txt", "at") as volumes_file:
             print(file=volumes_file)
             print(f" {today}, {width_tire}, {aspect_tire}, {volume_tire}",file=volumes_file)

     entrance = input("Write QUITE if you want to exit: ")
     entrance = entrance.lower()





