def read_input(n):
    # file = open('sample-io/sudoku_checker_sample_ts1_inputs.txt', 'r')
    file = open('test.txt', 'r')
    lines = file.readlines()
    number_of_cases = 0

    for line in lines:
        # Read the number of test cases
        number_of_cases = int(lines[0])

        for i in range(0, number_of_cases):
            line = 1 + (i*9) # TODO: Fix this

            # Read the number of rows and columns
            n = int(lines[1]) # TODO: Fix this

            # Read the number lines as string
            numbers_str_list = []
            for j in range(0, n*n):
                numbers_str_list.append(lines[2+j])

            # Convert the string list to int list
            numbers_list = []

    file.close()
    print(numbers_list)


if __name__ == '__main__':
    read_input