"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
09 Prove Assignment: Dictionaries
Purpose: Prove that you can write a Python program that reads CSV files and creates, populates, and uses a dictionary.
____________________________________________________________________

A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer’s requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.⋮

During this milestone, you will write half of a Python program named receipt.py that prints to the terminal window a receipt for a customer’s grocery order. Specifically, by the end of this milestone, your program must contain at least these two functions:

main
read_dictionary
and must read and process these two CSV files:

The products.csv file is a catalog of all the products that the grocery store sells.
The request.csv file contains the items ordered by a customer.

Exceeding the Requirements
Write code to discount the product prices by 10% if today is Tuesday or Wednesday.
In this program I created the if statement
#If num = 0 => Monday, num = 1 => Tuesday, etc
which I used num = date.today().weekday() to find the weekday
This part of code gives a discount of 10% if the week day is Tuesday (num = 1)
or Wednesday (num = 2)

I could have made the other requirement if I had
more time this week
I had to review a lot of concepts to do my program but it was amazing.
"""

import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import date
from datetime import datetime



def main():
    try:
        # The column headings and indexes.
        I_NUMBER_INDEX = 0
        NAME_INDEX_DICT = 1
        PRICE_INDEX_DICT = 2

        # Indexes of some of the columns
        # in the dentists.csv file.
        PRODUCT_NAME_INDEX = 0
        QUANTITY_INDEX = 1

        # Compute and print the sales tax amount. Use 6% as the sales tax rate.
        SALES_TAX_RATE = 0.06

        # Read the contents of a CSV file named students.csv
        # into a dictionary named students_dict. Use the I-Number
        # as the key in the dictionary.
        print("Inkom Emporium")
        products_dict = read_dictionary("products.csv", I_NUMBER_INDEX)
       # print("All Products")
       # print(products_dict)
        print()


        # Call the now() method to get the current
        # date and time as a datetime object from
        # the computer's operating system.

        product_list = []

        # Read each row in the CSV file one at a time.
            # The reader object returns each row as a list.
        

        # Open a file named dentists.csv and store a reference
        # to the opened file in a variable named dentists_file.
        with open("request.csv", "rt") as request_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(request_file)

            # The first row of the CSV file contains column
            # headings and not data about a dental office,
            # so this statement skips the first row of the
            # CSV file.
            next(reader)
            for row_list in reader:
                # For the current row, retrieve the
                # values in columns 0, 1.
                product_name = row_list[PRODUCT_NAME_INDEX]
                quantity = int(row_list[QUANTITY_INDEX])
                product_list.append(product_name)
                product_list.append(quantity)
        
        #print(product_list)
        #print()
        #print(f"Requested Items")
        #print()

        number_items = 0
        subtotal = 0

        for i in range(int(len(product_list)/2)):
            for key, value in products_dict.items():
                if product_list[2*i] == key and 2*i < len(product_list):
                    product_quant = product_list[2*i+1]
                    product_name = value[NAME_INDEX_DICT]
                    product_price = value[PRICE_INDEX_DICT]
                    number_items += product_quant
                    subtotal += product_quant * float(product_price)
                    sales_tax = subtotal * SALES_TAX_RATE
                    total = subtotal + sales_tax
                    print(f"{product_name}: {product_quant} @ {product_price}")

         # If num = 0 => Monday, num = 1 => Tuesday, etc
        num = date.today().weekday()
        # print(num)
        # This part of code gives a discount of 10% if the week day is Tuesday (num = 1)
        # or Wednesday (num = 2)
        if num == 1 or num == 2:
            subtotal = 0.9 * subtotal
            sales_tax = subtotal * SALES_TAX_RATE
            total = subtotal + sales_tax

        print()
        print(f"Number Items: {number_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        current_date_and_time = datetime.now()
        current_date = current_date_and_time.ctime()
        
        # Use an f-string to print the current
        # day of the week and the current time.
        # print(f"{current_date_and_time:%A %I:%M %p}")
        print(f"{current_date}")
        print()

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print("Error: missing file")
        print("[Errno 2] No such file or directory: 'products.csv'.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
                " the line number.")

    except IndexError as index_err:
        # This code will be executed if the user enters a valid
        # integer for the line number, but the integer is greater
        # than the number of lines in the file.
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        length = len(text_lines)
        if linenum < 0:
            print(f"{linenum} is a negative integer.")
        else:
            print(f"{linenum} is greater than the number" \
                    f" of lines in {filename}.")
            print(f"There are only {length} lines in {filename}.")
        print(f"Run the program again and enter a line number" \
                f" between 1 and {length}.")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")

    

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
