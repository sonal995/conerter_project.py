print("===== Simple Converter Project =====")

while True:
    print("\nChoose a Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9 / 5) + 32
        print("Fahrenheit =", round(f, 2))

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5 / 9
        print("Celsius =", round(c, 2))

    elif choice == "3":
        km = float(input("Enter distance in Kilometers: "))
        miles = km * 0.621371
        print("Miles =", round(miles, 2))

    elif choice == "4":
        miles = float(input("Enter distance in Miles: "))
        km = miles / 0.621371
        print("Kilometers =", round(km, 2))

    elif choice == "5":
        kg = float(input("Enter weight in Kilograms: "))
        pounds = kg * 2.20462
        print("Pounds =", round(pounds, 2))

    elif choice == "6":
        pounds = float(input("Enter weight in Pounds: "))
        kg = pounds / 2.20462
        print("Kilograms =", round(kg, 2))

    elif choice == "7":
        print("Thank you for using the Converter Project!")
        break

    else:
        print("Invalid choice! Please try again.")