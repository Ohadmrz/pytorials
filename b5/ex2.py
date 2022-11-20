colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']


def unique_colors(colors: list[str]) -> set:
    ret_val = set()
    for color in colors:
        ret_val.add(color.lower())
    return ret_val

c1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
c2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']

def colors_intersection(colors1: list[str], colors2: list[str]) -> set[str]:
    return unique_colors(colors1).intersection(unique_colors(colors2))

# def unique_colors(colors: list[str], num: int ) -> set:
#     print(colors)
#     print(num)
#     num = 50
#     colors = []
#     colors[0] = "blabla"
#     print("inside func", colors)

#
# def unique_colors(colors: list[str], num: int ) -> set:
#     for i, c in enumerate(colors):
#         colors[i] = c.lower()



# my_num = 100
# unique_colors(colors_2, my_num)
# print(my_num)
# print("outside func", colors_2)
