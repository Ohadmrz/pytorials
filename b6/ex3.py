def insert_persons(num: int) -> dict:
    persons = {}
    fields = ('id', 'first_name', 'phone')
    for i in range(num):
        person = {}
        for field in fields:
            person[field] = input(f"Insert {field}: ")
        persons[person['id']] = person
    return persons

print(insert_persons(2))