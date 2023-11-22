""" In your water_flow.py program, write a function named water_column_height that calculates and returns the height of a column of water from a tower height and a tank wall height. The function must have this header: 
"""
""""
Inside the functions of your water_flow.py program, you may have typed numbers for Earth’s acceleration of gravity, the density of water, and the dynamic viscosity of water. Instead of using the numbers inside your functions, define the following constants outside your functions. Then use the constant names in place of the numbers inside your functions.
Name	Value
EARTH_ACCELERATION_OF_GRAVITY	9.80665
WATER_DENSITY	998.2
WATER_DYNAMIC_VISCOSITY	0.0010016
"""
EARTH_ACCELERATION_OF_GRAVITY =	9.80665
WATER_DENSITY =	998.2
WATER_DYNAMIC_VISCOSITY	= 0.0010016
CONVERT_KPA_TO_PSI = 0.145038

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    pressure_psi = kPa_from_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} psi")




def water_column_height(tower_height, tank_height):
    """
     In your function, use the following formula for calculating the water column height.

     h = t + 3w/4
     where
     h is height of the water column
     t is the height of the tower
     w is the height of the walls of the tank that is on top of the tower
     """
    water_height = tower_height + 0.75 * tank_height
    return water_height


def pressure_gain_from_water_height(height):
    """
    In your function, use the following formula for calculating pressure caused by Earth’s gravity.

    P = ρgh/1000
    where
    P is the pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
     g is the acceleration from Earths gravity (9.80665 meter / second2)
    h is the height of the water column in meters
    """
    pressure = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
    return pressure


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_veloc):
   """
    In your function, use the following formula for calculating pressure loss from friction within a pipe.
    P = -f * L* ρ vˆ2 / (2000*d)
    where
    P is the lost pressure in kilopascals
    f is the pipe’s friction factor
    L is the length of the pipe in meters
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    d is the diameter of the pipe in meters
   """
   pressure_loss = (- friction_factor * pipe_length * WATER_DENSITY * fluid_veloc**2) / (2000 * pipe_diameter)
   return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    In your function, use the following formula for calculating pressure loss from pipe fittings.
    P = −0.04* ρ vˆ2*n / 2000 
    where
    P is the lost pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    n is the quantity of fittings  
    """
    pressure_loss_fittings = -0.04 * 998.2 * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss_fittings


def reynolds_number(hydraulic_diameter,fluid_velocity):
    """"
    In your function, use the following formula for calculating the Reynolds number.
    R = ρdv /μ
    where
    R is the Reynolds number
    ρ is the density of water (998.2 kilogram / meter3)
    d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
    v is the velocity of the water flowing through the pipe in meters / second
    μ is the dynamic viscosity of water (0.0010016 Pascal seconds)
    """
    reynoldsnumber = WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY
    return reynoldsnumber


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter): 
    """
    In your function, use the following two formulas for calculating pressure loss from a rounded reduction in a pipe’s diameter.
    k = (0.1 +50/R) * ((D/d)ˆ4-1)
    P = − k ρ vˆ2/2000
    where
    k is a constant computed by the first formula and used in the second formula
    R is the Reynolds number that corresponds to the pipe with the larger diameter
    D is the diameter of the larger pipe in meters
    d is the diameter of the smaller pipe in meters
    P is the lost pressure kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the larger diameter pipe in meters / second
    """
    k = (0.1 + 50/reynolds_number) * ((larger_diameter/smaller_diameter)**4 - 1)
    pressure_loss_reduction = (-k * WATER_DENSITY * fluid_velocity**2) / 2000
    return pressure_loss_reduction


def kPa_from_psi(pressure):
    pressure_psi = CONVERT_KPA_TO_PSI * pressure
    return pressure_psi

if __name__ == "__main__":
    main()