# 
# Function to find the maximum value in a matrix
def find_max_value(matrix):
    max_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

# Without using a function
matrix = [
    [3, 8, 1],
    [9, 2, 5],
    [4, 7, 6]
]

max_value = matrix[0][0]
for row in matrix:
    for value in row:
        if value > max_value:
            max_value = value

print("Maximum value (with function):", find_max_value(matrix))
print("Maximum value (without function):", max_value)