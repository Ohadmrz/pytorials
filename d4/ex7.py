import pprint


def my_key(student_data):
    if not student_data['grades']:
        avg_grade = 0
    else:
        avg_grade = sum(student_data['grades']) / len(student_data['grades'])
    name = student_data['name']
    return -avg_grade, name
    # return 100-avg_grade, name


if __name__ == '__main__':
    students = [
        {'name': 'moshe', 'grades': [50, 80, 100, 87, 70]},
        {'name': 'david', 'grades': [98, 83, 57]},
        {'name': 'yaffa', 'grades': [50, 98]},
        {'name': 'ron', 'grades': []},
        {'name': 'mathew', 'grades': [50, 80, 100, 87, 70]},
        {'name': 'jack', 'grades': [77, 90, 87, 70]},
        {'name': 'ran', 'grades': [89, 77, 78, 87, 100]},
        {'name': 'nir', 'grades': [56, 67, 100, 89]},
        {'name': 'mike', 'grades': [50, 80, 100, 87, 70]}
    ]

    pprint.pprint(sorted(students, key=my_key))

# print("apple" < 'orange')
# print("apple" < 'arm')
# print((4, 5) < (10, 30))
# print((4, 5) < (4, -30))
# print((4, 'apple') < (4, 'orange'))


