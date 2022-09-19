numbers_list = []


def read_input(n):
    file1 = open('sample-io/sudoku_checker_sample_ts1_inputs.txt', 'r')
    lines = file1.readlines()
    number_of_cases = 0

    for line in lines:
        # Read the number of test cases
        number_of_cases = int(lines[0])

        # Read the number of rows and columns
        n = int(lines[1+number_of_cases])
        for i in range(0, number_of_cases):
            for i in range(0, n):
                numbers_list.append(int(line.strip()))


    print(numbers_list)


if __name__ == '__main__':
    read_input