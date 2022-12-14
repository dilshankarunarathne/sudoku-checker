ideal_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lines = []
vert_lines = []
squares = []


def clear():
    lines.clear()
    vert_lines.clear()
    squares.clear()


if __name__ == '__main__':
    with open('test_big.txt', 'r') as f:
        # Read the number of cases
        number_of_cases = int(f.readline())
        # print('num cases = ', number_of_cases) # DEBUG

        for case in range(number_of_cases):
            flag = True

            # ==== READ DATA ====

            # Read N for case
            n = int(f.readline())
            # print('n = ', n) # DEBUG

            # For N*N times
            for line in range(n * n):
                # Read the line
                lines.append(f.readline().split())
                # print('line = ', lines[line]) # DEBUG

            # ==== FILL DATA ====

            # Fill vertical lines
            for i in range(n * n):
                vert_lines.append([])
                for j in range(n * n):
                    vert_lines[i].append(lines[j][i])
            # print('vert_lines = ', vert_lines) # DEBUG

            # Fill squares
            for i in range(n * n):
                squares.append([])
                for j in range(n * n):
                    squares[i].append(lines[i][j])
            # print('squares = ', squares) # DEBUG

            # ==== PROCESS DATA ====

            # Check if the horizontal lines are valid

            # For N*N times
            for i in range(n * n):
                if not (ideal_set == sorted(lines[i])):
                    # print('squares[i] = ', squares[i]) # DEBUG
                    flag = False
                    break

            # Check if the vertical lines are valid

            # For N*N times
            for i in range(n * n):
                if not (ideal_set == sorted(vert_lines[i])):
                    # print('squares[i] = ', squares[i]) # DEBUG
                    flag = False
                    break

            # Check if the squares are valid

            # For N*N times
            for i in range(n * n):
                if not (ideal_set == sorted(squares[i])):
                    # print('squares[i] = ', squares[i]) # DEBUG
                    flag = False
                    break

            # ==== FINAL CHECK ====

            if flag:
                print('Case #{}: YES'.format(case + 1))
            else:
                print('Case #{}: NO'.format(case + 1))

        clear()
