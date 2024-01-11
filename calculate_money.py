import math

def main():
    print("Write the taxe (%), time (years) and the amount of money wished (dollars) to simulate a loan")
    rate = float(input("Print the rate in % (0 - 100) "))
    year = int(input("Print the number of years (0 - 100) "))
    amount = float(input("Print the amount of money loan (0 - 1000000) "))
    print(f"rate {rate}")
    print(f"year {year}")
    print(f"amount of money {amount}")

    monthly_paymnent = calculate_moneypayment(rate,year,amount)
    print(f"The monthy payment is {monthly_paymnent:.2f}")

    print("Write the taxe (%), time (years) and the amount of money (dollars) that you plain to have in the future in order to simulate a retirement ")
    rate = float(input("Print the rate in % (0 - 100) "))
    year = int(input("Print the number of years (0 - 100) "))
    amount = float(input("Print the amount of money wished in the future (0 - 10000000) "))
    print(f"rate {rate}")
    print(f"year {year}")
    print(f"amount of money {amount}")

    monthly_saving = calculate_moneysaving(rate,year,amount)
    print(f"The monthy payment is {monthly_saving:.2f}")


def calculate_moneypayment(rate,year,amount):
        """Compute the approximate payment monthly of a loan."""
        try:
            r = rate
            n = year
            v = amount
            # Compute the amount of money you need to pay every month for a loan (v) in dollars.
            p = (v * r/1200 ) / (1 - (1/(1+r/1200))**(12 * n))        

        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            print("The values have to be integer or float")
        return p


def calculate_moneysaving(rate,year,amount):
        """Compute the approximate payment monthly of a loan."""
        try:
            r = rate
            n = year
            v = amount
            # Compute the amount of money you need to salve every month for having a determined amount of money (v) in dollars.
            p = (v * r/1200 ) / ((1+r/1200)**(12 * n)-1)       

        except ValueError:
            # When the user deletes all the digits in one
            # of the number entries, clear the result.
            print("The values have to be integer or float")
        return p

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
