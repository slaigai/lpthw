
def original_code():
    i = 0
    numbers = []

    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


def drill1(stop):
    """Accept stop number as arg"""
    i = 0
    numbers = []

    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


def drill3(stop, step):
    """Accept stop number and step number as arg"""
    i = 0
    numbers = []

    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


def drill5(stop, step):
    """Use a for loop and range function"""
    numbers = []
    for i in range(0, stop, step):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


def main():
    drill5(11, 2)


if __name__ == "__main__":
    main()
