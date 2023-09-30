"""
def compute(x, y, z):
    x = 7
x = 7
result = compute(3, 2, x)
print(f"{result[0]}")
"""

def kilometers_from_miles(miles):
    """Convert a value in miles to kilometers
    and return the kilometers value.
    """
    miles = float(input("Please enter a distance in miles: "))
    km = miles * 1.60934
    return km