def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
        
            heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1

        stack = []
        for j in range(n):
            while stack and heights[j] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(j)

        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

    return max_area

matrix = [["0"]]
output = maximalRectangle(matrix)
print(output)  
