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

        # For N*N times
        for line in range(n*n):
            # Read the line
            lines.append(f.readline().split())
            print('line = ', lines[line])

for x in lines[0]:
    sum += i

print('first line sum = ', sum)

