data = []
lines = []

with open('test.txt', 'r') as f:

    # Read the number of cases
    number_of_cases = int(f.read())
    print(number_of_cases)

    for line in f:

        # For each case...
        for i in range(number_of_cases):
            # Read N
            for number in f.readline():
                data.append(int(number))

            # # For N lines...
            # for j in range(n):
            #     # Read one line
            #     line = f.readline().split()
            #     print (line)

