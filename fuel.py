def main():
    fuel_left = input("How much fuel do you have left? ")
    percent = convert(fuel_left)
    fuel = gauge(percent)
    print(fuel)


def convert(fraction):
        x, y = fraction.split("/")
        if int(x)/int(y) > 1:
            raise ValueError
        elif int(y) == 0:
             raise ZeroDivisonError
        return int(int(x)/int(y) * 100)


def gauge(fuel):
    if fuel >= 0 and fuel <= 1:
        return "E"
    elif fuel >= 99 and fuel <= 100:
        return "F"
    elif fuel > 1 and fuel < 99:
        return str(int(fuel)) + "%"


if __name__ == "__main__":
    main()


