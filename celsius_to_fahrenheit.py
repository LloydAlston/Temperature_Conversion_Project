def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        c = float(input("Enter temperature in °C: "))
        print(f"Result: {celsius_to_fahrenheit(c):.2f} °F")

    elif choice == 2:
        c = float(input("Enter temperature in °C: "))
        print(f"Result: {celsius_to_kelvin(c):.2f} K")

    elif choice == 3:
        f = float(input("Enter temperature in °F: "))
        print(f"Result: {fahrenheit_to_celsius(f):.2f} °C")

    elif choice == 4:
        f = float(input("Enter temperature in °F: "))
        print(f"Result: {fahrenheit_to_kelvin(f):.2f} K")

    elif choice == 5:
        k = float(input("Enter temperature in K: "))
        print(f"Result: {kelvin_to_celsius(k):.2f} °C")

    elif choice == 6:
        k = float(input("Enter temperature in K: "))
        print(f"Result: {kelvin_to_fahrenheit(k):.2f} °F")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
