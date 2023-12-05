from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    window = deque()

    for i, num in enumerate(nums):
        
        while window and window[0] < i - k + 1:
            window.popleft()


        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
output = maxSlidingWindow(nums, k)
print(output)
