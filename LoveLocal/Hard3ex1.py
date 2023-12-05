def count_digit_one(n):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count

n = 13
output = count_digit_one(n)
print(output)
