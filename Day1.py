import time


def read_file_to_list(filename):
    file_list = []
    with open(filename, 'r') as f:
        for line in f:
            file_list.append(line.strip("\n\r"))
    return file_list


# parse out the into two lists of numbers, then order them
def day1_parser(input_array):

    locations_a = []
    locations_b = []
    for line in input_array:
        locations_a.append(int(line.split("   ")[0]))
        locations_b.append(int(line.split("   ")[1]))
    locations_a.sort()
    locations_b.sort()
    return locations_a, locations_b


# compare the two location lists in order and find the absolute difference between all the pairs
def day1(first_list, second_list):

    result = 0
    for i in range(len(first_list)):
        result = result + abs(first_list[i] - second_list[i])
    return result


def day1_p2(first_list, second_list):

    result = 0
    for i in range(len(first_list)):
        copies = len([x for x in second_list if x == first_list[i]])
        result = result + (first_list[i] * copies)
    return result

# for each item in the first list, now see if it's in the second list, and how many times
def main():
    print("Advent of Code Day 1")

    do_part_1 = True
    do_part_2 = True
    start = time.time()

    if do_part_1:
        print("Part 1")
        input_array = read_file_to_list("InputFiles/day1_p1_actual")
        locations_a, locations_b = day1_parser(input_array)
        print(f"Value is: {day1(locations_a, locations_b)}")

    if do_part_2:
        print("Part 2")
        print(f"Value is: {day1_p2(locations_a, locations_b)}")

    end = time.time()

    print(f"{end-start:.3f} seconds")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
