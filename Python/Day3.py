import re


def read_input(data):
    with open(data, "r") as file:
        return file.read()


def find_pattern(data):
    pattern = re.compile(r"(do|don't|mul)\((\d*),?(\d*)\)")

    matches = [(match.group(1), match.group(2), match.group(3), match.start())
               for match in pattern.finditer(data)]

    matches.sort(key=lambda match: match[3])

    matches = [(match[0], match[1], match[2]) for match in matches]
    return matches


def process_command(data):
    result = 0
    do = True
    for command, x, y, in data:
        if command == "mul":
            if do:
                result += int(x) * int(y)
        elif command == "do":
            do = True
        elif command == "don't":
            do = False
    return result


def main():
    data = read_input("Day3.txt")
    operations = find_pattern(data)
    result = process_command(operations)
    print(result)


if __name__ == "__main__":
    main()
