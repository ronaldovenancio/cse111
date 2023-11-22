"""
____________________________________________________________________
Author: Ronaldo Venancio
Assignments in CSE 111
08 Prove Assignment: Dictionaries
Purpose: Prove that you can write a Python program that uses a dictionary and lists.
____________________________________________________________________

In the chemistry.py file, write a function named make_periodic_table that takes no parameters and creates and returns a compound list. The compound list must contain all the data in the table of elements shown in the Table of Elements section above. The data within the compound list must be organized like this:
    periodic_table_list = [
        # [symbol, name, atomic_mass]
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
          ⋮
    ]


In this program I created the funciton  get_formula_name(formula, known_molecules_dict) and I used the dictionary known_molecules_dist 
I prefered this part of requirements because it was a bit simple for me but I think that I could have made the other requirement if I had
more time this week
I had to review a lot of concepts to do my program but it was amazing.
"""
# Start this program by
# calling the main function.

from formula import parse_formula

known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }
    
def main():
    """
    table_list = make_periodic_table()
    for element in table_list:
        print(f"{element[1]}   {element[2]}")
    """

    # Get a chemical formula for a molecule from the user.

    formula = input(f"Enter the molecular formula of the sample, like for exmaple, C6H6: ")

    # Get the mass of a chemical sample in grams from the user.

    mass = float(input(f"Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula,periodic_table)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample.
    moles = mass/molar_mass

    # Print the molar mass.
    print(f" The molar mass is {molar_mass}")

    # Print the number of moles.
    print(f" The moles number is {moles}")

    chemical_mol = get_formula_name(formula, known_molecules_dict)

    



def make_periodic_table():
    periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "Ac":   ["Actinium", 227],
        "Ag":   ["Silver", 107.8682],
        "Al":   ["Aluminum", 26.9815386],
        "Ar":   ["Argon", 39.948],
        "As":   ["Arsenic", 74.9216],
        "At":   ["Astatine",	210],
        "Au":   ["Gold",	196.966569],
        "B":    ["Boron", 10.811],
        "Ba":   ["Barium", 137.327],
        "Be":   ["Beryllium", 9.012182],
        "Bi":   ["Bismuth",	208.9804],
        "Br":	["Bromine",	79.904],
        "C":	["Carbon",	12.0107],
        "Ca":	["Calcium",	40.078],
        "Cd":	["Cadmium",	112.411],
        "Ce":	["Cerium",	140.116],
        "Cl":	["Chlorine",	35.453],
        "Co":	["Cobalt",	58.933195],
        "Cr":	["Chromium",	51.9961],
        "Cs":	["Cesium",	132.9054519],
        "Cu":	["Copper",	63.546],
        "Dy":	["Dysprosium", 162.5],
        "Er":	["Erbium",	167.259],
        "Eu":	["Europium",	151.964],
        "F":	["Fluorine",	18.9984032],
        "Fe":	["Iron",	55.845],
        "Fr":	["Francium",	223],  
        "Ga":	["Gallium",	69.723],
        "Gd":	["Gadolinium",	157.25],
        "Ge":	["Germanium",	72.64],
        "H":	["Hydrogen",	1.00794],
        "He":	["Helium",	4.002602],
        "Hf":	["Hafnium",	178.49],
        "Hg":	["Mercury",	200.59],
        "Ho":	["Holmium",	164.93032],
        "I":	["Iodine",	126.90447],
        "In":	["Indium",	114.818],
        "Ir":	["Iridium",	192.217],
        "K":	["Potassium",	39.0983],
        "Kr":	["Krypton",	83.798],
        "La":	["Lanthanum",	138.90547],
        "Li":	["Lithium",	6.941],
        "Lu":	["Lutetium",	174.9668],
        "Mg":	["Magnesium",	24.305],
        "Mn":	["Manganese",	54.938045],
        "Mo":	["Molybdenum",	95.96],
        "N":	["Nitrogen",	14.0067],
        "Na":	["Sodium",	22.98976928],
        "Nb":	["Niobium",	92.90638],
        "Nd":	["Neodymium",	144.242],
        "Ne":	["Neon",	20.1797],
        "Ni":	["Nickel",	58.6934],
        "Np":	["Neptunium",	237],
        "O":	["Oxygen",	15.9994],
        "Os":	["Osmium",	190.23],
        "P":	["Phosphorus",	30.973762],
        "Pa":	["Protactinium",	231.03588],
        "Pb":   ["Lead",	207.2], 
        "Pd":	["Palladium",	106.42],
        "Pm":	["Promethium",	145],
        "Po":	["Polonium",	209],
        "Pr":	["Praseodymium",	140.90765],
        "Pt":	["Platinum",	195.084],
        "Pu":	["Plutonium",	244],
        "Ra":	["Radium",	226],
        "Rb":	["Rubidium",	85.4678],
        "Re":	["Rhenium",	186.207],
        "Rh":	["Rhodium",	102.9055],    
        "Rn":	["Radon",	222],
        "Ru":	["Ruthenium",	101.07],
        "S":	["Sulfur",	32.065],
        "Sb":	["Antimony",	121.76],
        "Sc":	["Scandium",	44.955912],
        "Se":	["Selenium",	78.96],
        "Si":	["Silicon",	28.0855],
        "Sm":	["Samarium",	150.36],
        "Sn":	["Tin",	118.71],
        "Sr":	["Strontium",	87.62],   
        "Ta":	["Tantalum",	180.94788],
        "Tb":	["Terbium",	158.92535],
        "Tc":	["Technetium",	98],
        "Te":	["Tellurium",	127.6],
        "Th":	["Thorium",	232.03806],
        "Ti":	["Titanium",	47.867],
        "Tl":	["Thallium",	204.3833],
        "Tm":	["Thulium",	168.93421],
        "U":	["Uranium",	238.02891],
        "V":	["Vanadium",	50.9415],
        "W":	["Tungsten",	183.84],
        "Xe":	["Xenon",	131.293],
        "Y":	["Yttrium",	88.90585],
        "Yb":	["Ytterbium",	173.054],
        "Zn":	["Zinc",	65.38],
        "Zr":	["Zirconium",	91.224]
    }
    """
    new_list = []
    for element_list in periodic_table_list:
        list= [element_list[1], element_list[2]]
        new_list.append(list)
    return new_list
    """
   # print(periodic_table_dict)
    return periodic_table_dict




    # Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    
    mass_molar = 0

    for element in symbol_quantity_list:
        element_name = element[SYMBOL_INDEX]
        element_quant = element[QUANTITY_INDEX]
        for symbol, atomic_mass in periodic_table_dict.items():
            if element_name == symbol:
                mass_molar += element_quant * atomic_mass[QUANTITY_INDEX] 

    # Return the total molar mass.
    return mass_molar


known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }



def get_formula_name(formula, known_molecules_dict):
    """
    Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    he name of the chemical formula; otherwise return
    "unknown compound".
    
         
    Parameters
    formula is a string that contains a chemical formula
    known_molecules_dict is a dictionary that contains
    known chemical formulas and their names
    Return: the name of a chemical formula
    """
    count_yes = 0
    count_not = 0
    
    for formula_molec, molecula_name in known_molecules_dict.items():
         chemical_formula = molecula_name
         if formula == formula_molec:
            count_yes += 1
            # print(f"{formula} is in the know_molecules_dict")
    else:
        count_not +=1
        #print(f"{formula} is unknown compound")
    if count_yes == 1:
         print(f"{formula} is in the know_molecules_dict")
    if count_not != 0 and count_yes != 1:
         print(f"{formula} is unknown compound")


    return chemical_formula



if __name__ == "__main__":
    main()

