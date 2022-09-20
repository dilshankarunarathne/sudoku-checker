data = []

f = open("test.txt", "r")
print(f.read())
f.close()

# with open('test.txt', 'r') as f:
#     for line in f:
#
#         # Read the number of cases
#         number_of_cases = int(f.readline())
#
#         # For each case...
#         for i in range(number_of_cases):
#             # Read N
#             n = int(f.readline())
#
#             # For N lines...
#             for j in range(n):
#                 # Read one line
#                 line = f.readline().split()
#                 print (line)

