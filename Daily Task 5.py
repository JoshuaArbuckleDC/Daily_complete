# Daily Task 5
# Joshua Arbuckle (100833522)
# TPRG-2131
# September 20, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

import math

# Calculate the resonant frequency, bandwidth, and Q factor for a SERIES resonant circuit
def series_resonance(i, c, r):
    resonant_frequency = 1 / (2 * math.pi * math.sqrt(i / 1000 * c / 1000000))
    bandwidth = r / (i / 1000)
    q_factor = 1 / r * math.sqrt((i / 1000) / (c / 1000000))
    return resonant_frequency, bandwidth, q_factor

# Calculate the total resistance for two resistors in parallel
def parallel_resistance(resistor1, resistor2):
    total_resistance = 1 / (1 / resistor1 + 1 / resistor2)
    return total_resistance

# Calculate the RC time constant
def rc_time_constant(r, c):
    time_constant = r * c
    return time_constant

# Calculate the resonant frequency and Q factor for a series RLC circuit
def series_rlc_resonance(l, c, r):
    resonant_frequency = 1 / (2 * math.pi * math.sqrt(l / 1000 * c / 1000000))
    q_factor = 1 / (2 * math.pi * resonant_frequency * r / 1000)
    return resonant_frequency, q_factor

def get_positive_value(message):
    value = float(input(message))
    while value <= 0.0:
        value = float(input("The value must be greater than zero\n" + message))
    return value

print("Resonant circuit and resistor calculator")
print("(Enter 'q' to quit)")

while True:
    print("Choose an option:")
    print("1. Calculate total resistance for two resistors in parallel")
    print("2. Calculate RC time constant")
    print("3. Calculate SERIES RLC resonance and Q factor")
    print("Q. Quit")
    choice = input("Enter your choice (1, 2, 3, or Q): ")

    if choice == "1":
        resistor1 = get_positive_value("Enter the value of the first resistor in ohms: ")
        resistor2 = get_positive_value("Enter the value of the second resistor in ohms: ")
        total_resistance = parallel_resistance(resistor1, resistor2)
        print(f"Total Resistance (in parallel): {total_resistance} ohms\n")

    elif choice == "2":
        resistor = get_positive_value("Enter the value of the resistor in ohms: ")
        capacitance = get_positive_value("Enter the value of the capacitance in uF: ")
        time_constant = rc_time_constant(resistor, capacitance)
        print(f"RC Time Constant: {time_constant} seconds\n")

    elif choice == "3":
        inductance = get_positive_value("What is the inductance in mH? ")
        capacitance = get_positive_value("What is the capacitance in uF? ")
        resistance = get_positive_value("What is the resistance in ohms? ")
        resonant_frequency, q_factor = series_rlc_resonance(inductance, capacitance, resistance)
        print(f"Resonant Frequency for Series RLC Circuit: {resonant_frequency} Hz")
        print(f"Q Factor: {q_factor}\n")

    elif choice.lower() == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or Q.")
