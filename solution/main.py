ideal_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

lines = []
vert_lines = []
squares = []


def clear():
    lines.clear()
    vert_lines.clear()
    squares.clear()


def checker() -> bool:
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
                    return False

            # Check if the vertical lines are valid

            # For N*N times
            for i in range(n * n):
                if not (ideal_set == sorted(vert_lines[i])):
                    return False

            # Check if the squares are valid

            # For N*N times
            for i in range(n * n):
                if not (ideal_set == sorted(squares[i])):
                    return False

        clear()


if __name__ == '__main__':
    sudoku = checker()
    if sudoku:
        print("Sudoku is not valid")
    else:
        print("Sudoku is valid")
