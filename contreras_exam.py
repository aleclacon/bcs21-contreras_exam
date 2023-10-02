highest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def find(matrix):
    max = float('-inf')
    for row in matrix:
        for num in row:
            if num > max:
                max_value = num
    return max_value


max = find(highest)
print("MADE BY: CONTRERAS, ALeianna Clarisse C.")
print("The max value:", max)

for row in highest:
    for num in row:
        print(f"|{num}", end=" ")
    print("|")