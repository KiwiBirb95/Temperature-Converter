import sys


def main():
    print("Enter Minimum Temp")
    min_temp = int(input())
    print("Enter Max Temp")
    max_temp = int(input())
    temp_conversion(min_temp, max_temp)


def temp_conversion(min_temp, max_temp):
    for x in range(min_temp, max_temp + 1):
        print("celsius=", x, "fahrenheit=", conversion_formula(x))


def conversion_formula(cel):
    fah = cel * (9.0 / 5.0) + 32
    return fah


if __name__ == "__main__":
    sys.exit(main())

# This is a test comment
