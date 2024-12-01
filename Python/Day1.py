def input_to_lists(input):
    left_list = []
    right_list = []
    with open(input) as file:
        lines = file.readlines()
        for line in lines:
            left_list.append(int(line.split()[0]))
            right_list.append(int(line.split()[1]))
    return left_list, right_list


def sort_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def distance(left_list, right_list):
    # Could use a zip here
    # return sum(abs(l - r) for l, r in zip(left_list, right_list))
    total_distance = 0
    for index in range(len(left_list)):
        difference = abs(left_list[index] - right_list[index])
        total_distance += difference
    return total_distance


def similarity(left_list, right_list):
    total_score = 0
    for item in left_list:
        match_count = right_list.count(item)
        if match_count > 0:
            score = item * match_count
            total_score += score
    return total_score


def main():
    left_list, right_list = input_to_lists("input.txt")
    left_list, right_list = sort_lists(left_list, right_list)
    print("Distance: ", distance(left_list, right_list))
    print("Similarity: ", similarity(left_list, right_list))


if __name__ == "__main__":
    main()
