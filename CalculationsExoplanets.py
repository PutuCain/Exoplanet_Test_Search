import numpy as np
import pandas as pd

# Putting Universal Constants For Flow Ease
G = 6.67430e-11   # Gravitational Constant (m^3 kg^-1 s^-2)
MSUN = 1.989e30   # Mass of our Sun (in kg)
RSUN = 6.957e8    # Radius of our Sun (in meters)
RJUP = 7.1492e7   # Radius of Jupiter (in meters)
AU = 1.496e11     # 1 Astronomical Unit (in meters)


def period_csv():
    # This function reads the detected period from the CSV file and returns it as a float
    df = pd.read_csv("Exoplnet_Test1_Data/Detected_Planet_Period.csv")
    Value = str(df["Period days"].iloc[0])
    return float(Value)


def get_orbital_distance(period_days, mass_star):
    # This function calculates the orbital distance of a planet
    # Converting period_days to seconds for Kepler's Law
    period_seconds = period_days*24*60*60
    # Converting mass of the star in terms of solar mass
    mStar = mass_star*MSUN
    # Formulating 3rd law of Kepler
    a = ((G*mStar*(period_seconds**2))/(4*3.14**2))**(1/3)
    a = a/AU  # Converting into Astronomical Units
    return a


def get_transit_depth(radius_planet, radius_star):
    # This function calculates the transit depth of a planet
    # Converting radius of planet and star in terms of the radius of Jupiter abd The Sun
    rPlanet = radius_planet*RJUP
    rStar = radius_star*RSUN
    # Calculating transit depth using the formula (Rp/Rs)^2
    transit_depth = (rPlanet/rStar)**2
    return transit_depth


def get_equilibrium_temperature(stell_lum, distance_AU, tbaseline=255):
    # This function shall calculate the equilibrium temperature of the planet
    t_in_Kelvin = tbaseline * (stell_lum)**(1/4) * (distance_AU)**(-1/2)
    t_in_celsius = t_in_Kelvin - 273.15
    return t_in_celsius


def check_habitability_zone(distance_habitability, stell_lum):
    inner = 3/4*(np.pow(stell_lum, 1/2))
    outer = 1.77*(np.pow(stell_lum, 1/2))
    if distance_habitability >= inner and distance_habitability <= outer:
        return "Within the Goldilocks Zone"
    else:
        return "Unhabitable"


# Input Analysis
period_days = period_csv()
mass_star = float(input("Enter the mass of the star: "))
radius_planet = float(
    input("Enter the radius of the planet in terms of Jupiter's radius: "))
radius_star = float(
    input("Enter the radius of the star in terms of the Sun's radius: "))
stell_lum = float(
    input("Enter the luminosity of the star in terms of the Sun's luminosity: "))

# Execution
distance_habitability = get_orbital_distance(period_days, mass_star)
transit_depth = get_transit_depth(radius_planet, radius_star)
equilibrium_temperature = get_equilibrium_temperature(
    stell_lum, distance_habitability)
habitability_check = check_habitability_zone(distance_habitability, stell_lum)

# Ouput Declaration
print(f"The orbital distance of the planet is: {distance_habitability} AU")
print(f"The transit depth of the planet is: {transit_depth}")
print(
    f"The equilibrium temperature of the planet is: {equilibrium_temperature} °C")
print(f"The habitability status of the planet is: {habitability_check}")

if habitability_check == "Within the Goldilocks Zone":
    print("This planet is a potential candidate for habitability.")
    print("Conducting further analysis on its atmospheric constituents")


def analyze_atmosphere():
    # Gas detection
    m = input("Methane detected? (yes/no):  ").lower()
    o = input("Oxygen detected? (yes/no):  ").lower()
    w = input("Water vapor detected? (yes/no):  ").lower()
    c = input("Carbon dioxide detected? (yes/no):  ").lower()
    if m == "yes" and o == "yes" and w == "yes" and c == "yes":
        print("The presence of methane, oxygen, water vapor, and carbon dioxide suggests potential habitability.")
    elif (m == "yes" and o == "yes") or (m == "yes" and w == "yes") or (o == "yes" and w == "yes"):
        print("The presence of some key gases may indicate potential habitability, but further analysis is needed.")
    else:
        print("The absence of key gases may indicate a less hospitable environment.")
