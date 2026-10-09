
# Electrical Engineering Calculator
# Author: Eldulis
# Purpose: Perform basic electrical calculations

def ohms_law():
    print("\nOhm's Law Calculator")
    print("V = I × R")

    current = float(input("Enter current in amperes (A): "))
    resistance = float(input("Enter resistance in ohms (Ω): "))

    voltage = current * resistance

    print(f"Voltage = {voltage:.2f} V")

def electrical_power():
    print("\nElectrical Power Calculator")
    print("P = V × I")

    voltage = float(input("Enter voltage in volts (V): "))
    current = float(input("Enter current in amperes (A): "))

    power = voltage * current

    print(f"Power = {power:.2f} W")

def main():
    while True:
        print("\n=== Electrical Engineering Calculator ===")
        print("1. Calculate voltage using Ohm's law")
        print("2. Calculate electrical power")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            ohms_law()
        elif choice == "2":
            electrical_power()
        elif choice == "3":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
