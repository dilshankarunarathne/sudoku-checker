ideal_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lines = []
vert_lines = []
squares = []

with open('test.txt', 'r') as f:
    # Read the number of cases
    number_of_cases = int(f.readline())
    # print('num cases = ', number_of_cases) # DEBUG

    for case in range(number_of_cases):
        # ==== READ DATA ====

        # Read N for case
        n = int(f.readline())
        # print('n = ', n) # DEBUG

        # For N*N times
        for line in range(n * n):
            # Read the line
            lines.append(f.readline().split())
            # print('line = ', lines[line]) # DEBUG

        # ==== PROCESS DATA ====

        # Check if the horizontal lines are valid

        # For N*N times
        for i in range(n * n):
            print(ideal_set == sorted(lines[i]))
