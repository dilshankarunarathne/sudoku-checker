data = []
lines = []

with open('test.txt', 'r') as f:

    # Read the number of cases
    number_of_cases = int(f.readline())
    print('num cases = ', number_of_cases)

    for case in range(number_of_cases):
        # Read N for case
        n = int(f.readline())
        print('n = ', n)

