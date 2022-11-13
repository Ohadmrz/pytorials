# Write a program that receives a list of numbers, and prints the minimum number
nums = [56, 3, 23, 1, 0, 45, -1, 4, 2, 0]

min_num = None
for i in nums:
    if min_num is None:
        min_num = i
    elif min_num > i:
        min_num = i
print(min_num)