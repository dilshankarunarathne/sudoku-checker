data = []

with open('test.txt') as f:
    for line in f:

        # Read the number of cases
        number_of_cases = int(f.readline())

        # For each case...
        for i in range(number_of_cases):
            # Read N
            n = int(f.readline())

