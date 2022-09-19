
number_of_cases = 0
numbers_list = []


def read_input(n):
    file1 = open('sample-io/sudoku_checker_sample_ts1_inputs.txt', 'r')
    lines = file1.readlines()

    for line in lines:
        number_of_cases = int(lines[0])
        for i in range(0, n):
            numbers_list.append(int(line(i)))
    print(numbers_list)


if __name__ == '__main__':
    read_input