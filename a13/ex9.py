# num = int(input("Insert a num"))
# for i in range(2, num):
#     if num % i == 0:
#         # num is not a prime number
#         break
# if i == num-1:
#     # num is a prime number
#     print(f"{num} is prime")

# start_range = int(input("Insert the start of the range: "))
# end_range = int(input("Insert the end of the range: "))
# for num in range(start_range, end_range+1):
#     has_divisor = False
#     for i in range(2, num):
#         if num % i == 0:
#             # num is not a prime number
#             has_divisor = True
#             break
#
#     if not has_divisor:
#         # num is a prime number
#         print(f"{num} is prime")


# pass vs continue

# word = "Piano"
# for i, char in enumerate(word):
#     print(i, char)

word = "Piano"
# for t in enumerate(word):
#     print(t[0], t[1])
# i = 0
# for char in word:
#     print(i, char)
#     i += 1

# goods = [['apple', 'pear', 'peach', 'chery'],
#          ['skjahlkdjhglkjdfhg'],
#          ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#         'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]
#
# longest_name = ""
# external_idx = -1
# internal_idx = -1
# max_inner_len = 0
#
# for inx, fruits_list in enumerate(goods):
#     for j, fruit_str in enumerate(fruits_list):
#         fruit_len = len(fruit_str)
#         if fruit_len > max_inner_len:
#             max_inner_len = fruit_len
#             longest_name = fruit_str
#             external_idx = inx
#             internal_idx = j
#
# print(longest_name, max_inner_len, external_idx, internal_idx)


goods = [['apple', 'pear', 'peach', 'chery'],
         ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
          'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]

longest_len = 0
longest_items = []
longest_indexes = []

for i, inner_goods in enumerate(goods):
    for j, item in enumerate(inner_goods):
        item_len = len(item)
        if item_len > longest_len:
            longest_len = item_len
            longest_items = [item]
            longest_indexes = [[i, j]]
        elif item_len == longest_len:
            longest_items.append(item)
            longest_indexes.append([i, j])

print(longest_len)
print(longest_items)
print(longest_indexes)