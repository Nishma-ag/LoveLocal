def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    height = [0] * n
    left = [0] * n
    right = [n] * n
    max_area = 0
    
    for i in range(m):
        cur_left, cur_right = 0, n
    
        for j in range(n):
            if matrix[i][j] == '1':
                height[j] += 1
                left[j] = max(left[j], cur_left)
            else:
                height[j] = 0
                left[j] = 0
                cur_left = j + 1
        
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j
        
        for j in range(n):
            max_area = max(max_area, height[j] * (right[j] - left[j]))
    
    return max_area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
result = maximalRectangle(matrix)
print(result)
