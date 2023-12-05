def count_digit_one(n):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count


n = 0
output = count_digit_one(n)
print(output)
