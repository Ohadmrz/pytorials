COMMANDS = ("insert", "lookup", "quit")
bday_dict = {}


def get_command() -> str:
    while True:
        command = input("Insert command (insert, lookup, quit): ")
        if command not in COMMANDS:
            print("Invalid command, try again")
        else:
            return command


def insert_bday():
    name = input("Insert name: ")
    bday = input(f"Insert bday for {name}: ")
    bday_dict[name] = bday


def lookup_bday():
    name = input("Insert name: ")
    if name in bday_dict:
        print(f"{name}'s birthday is {bday_dict[name]}")
    else:
        print(f"Birth date for {name} does not exist")


while True:
    cmd = get_command()
    if cmd == "insert":
        insert_bday()
    elif cmd == "lookup":
        lookup_bday()
    else:
        print("Bye-bye")
        exit(0)


# commands = ("insert", "lookup", "quit")
# bday_dict = {}
#
# while True:
#     command = input("Insert command: ")
#
#     if command not in commands:
#         print("Invalid command, try again")
#         continue
#
#     if command == "insert":
#         name = input("Insert name: ")
#         bday = input("Insert birthday date: ")
#         bday_dict[name.lower()] = {"original_name": name, "date": bday}
#         print("The dictionary:", bday_dict)
#     elif command == "lookup":
#         lookup_name = input("Insert name to search: ").lower()
#         if lookup_name in bday_dict:
#             print(f"The date for {bday_dict[lookup_name]['original_name']} is: {bday_dict[lookup_name]['date']}")
#         else:
#             for key in bday_dict.keys():
#                 if lookup_name in key:
#                     print(f"We found {key}. Do you wwant his/her bday?")
#                     # continue here
#             print("The name does not exist")
#     elif command == "quit":
#         exit(0)