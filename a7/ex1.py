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