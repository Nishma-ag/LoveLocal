def count_ones(matrix):
    # Initialize a variable to store the count of 1s
    ones_count = 0
    
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            # Check if the element is '1'
            if element == '1':
                # Increment the count if the element is '1'
                ones_count += 1
    
    # Return the final count of 1s
    return ones_count

# Example usage
matrix = [["0", "1"], ["1", "0"]]
result = count_ones(matrix)
print(result)
