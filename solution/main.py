numbers_list = []


def read_input(n):
    file1 = open('sample-io/sudoku_checker_sample_ts1_inputs.txt', 'r')
    lines = file1.readlines()
    n = 0

    for line in lines:
        number_of_cases = int(lines[0])
        numbers_list.append(line.strip())
        for i in range(0, n):
            numbers_list.append(int(line.strip(i)))

        n = number_of_cases

    print(numbers_list)


if __name__ == '__main__':
    read_input