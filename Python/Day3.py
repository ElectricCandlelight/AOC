import re


def read_input(data):
    with open(data, "r") as file:
        return file.read()


def find_mul(data):
    return re.findall(r"mul\((\d+),(\d+)\)", data)


def multiply_add(data):
    result = 0
    for i in data:
        result += int(i[0]) * int(i[1])
    return result


def main():
    data = read_input("Day3.txt")
    data = find_mul(data)
    result = multiply_add(data)
    print(result)


if __name__ == "__main__":
    main()
