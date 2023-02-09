import sys


def main():
    print("Enter Minimum Temp:")
    min_temp = int(input())
    print("Enter Max Temp:")
    max_temp = int(input())
    temp_conversion(min_temp, max_temp)


# Converts Fahrenheit to Celsius
# def temp_conversion(min_temp, max_temp):
#     for x in range(min_temp, max_temp + 1):
#         print("Celsius =", x, "Fahrenheit =", conversion_formula(x))


# Converts Celsius to Fahrenheit
def temp_conversion(min_temp, max_temp):
    for x in range(min_temp, max_temp + 1):
        print("Fahrenheit =", x, "Celsius =", conversion_formula(x))


# Displays Fahrenheit to Celsius
# def conversion_formula(cel):
#     fah = cel * (9.0 / 5.0) + 32
#     return fah


# Displays Celsius to Fahrenheit
def conversion_formula(fah):
    cel = (5.0 / 9.0) * (fah - 32)
    return cel

if __name__ == "__main__":
    sys.exit(main())
