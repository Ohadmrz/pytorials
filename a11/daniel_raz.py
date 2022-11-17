"""
coffee_time.py

author: Daniel Raz (@druckhead)
date: 12/11/2022

A simple coffee order management system for you and your friends in your Hi-Tech offices
It accepts:
    A time of day
    The number of drinkers
    Option to offset the starting point for coffee choice
    Option to filter Coffee types to your satisfaction

It outputs:
    The type of coffee each office worker will get according to the provided inputs
"""

# tuple of coffee types to ensure immutability
coffee_types = ('Espresso', 'Doppio', 'Lungo', 'Ristretto',
                'Macchiato', 'Corretto', 'Con Panna', 'Romano',
                'Cappuccino', 'Americano', 'Café Late', 'Flat White',
                'Marocchino', 'Mocha', 'Bicerin', 'Breve',
                'Raf Coffee', 'Mead Raf', 'Vienna Coffee', 'Chocolate Milk',
                'Latte Macchiato', 'Glace', 'Freddo', 'Irish Coffee',
                'Frappe', 'Cappuccino Freddo', 'Caramel Frappe', 'Espresso Laccino'
                )

print("""
.-. . .-..----..-.    .---.  .----. .-.   .-..----.
| |/ \\| || {_  | |   /  ___}/  {}  \\|  `.'  || {_  
|  .'.  || {__ | `--.\\     }\\      /| |\\ /| || {__ 
`-'   `-'`----'`----' `---'  `----' `-' ` `-'`----'
                .---.  .----.                      
               {_   _}/  {}  \\                     
                 | |  \\      /                     
                 `-'   `----'                      
       .---.  .----. .----..----..----.            
      /  ___}/  {}  \\| {_  | {_  | {_              
      \\     }\\      /| |   | |   | {__             
       `---'  `----' `-'   `-'   `----'            
          .---. .-..-.   .-..----.                 
         {_   _}| ||  `.'  || {_                   
           | |  | || |\\ /| || {__                  
           `-'  `-'`-' ` `-'`----' 
""")

hours = minutes = None

is_valid_time = None
while is_valid_time is not True:
    time = input("Enter the current time (24-hour format): ")
    formatted_time = time.split(':')
    # validate that time is split with semicolon
    if len(formatted_time) == 2:
        # validate time is NOT negative
        if '-' in formatted_time[0] or '-' in formatted_time[1]:
            print(f"OverFlow Error: Invalid Time given.\n"
                  f"Hours and Minutes MUST be positive numbers\n")
            continue
        # validate Hours and Minutes do not contain any non-numeric characters
        if formatted_time[0].isnumeric() is not True or formatted_time[1].isnumeric() is not True:
            print("ValueError: This isn't a time!\n")
            continue
        hours = int(formatted_time[0])
        # validate hours are not over 24
        if hours > 24:
            print(f"OverFlow Error: Invalid Hour given.\n"
                  f"Hours Must be between 0 and 24\n")
            continue
        minutes = int(formatted_time[1])
        # validate minutes are not above 59
        if minutes > 59:
            print(f"OverFlow Error: Invalid Minutes given.\n"
                  f"Minutes Must be between 0 and 59\n")
            continue
        # passed all validations
        is_valid_time = True
    else:
        print("ValueError: This isn't a time!\n")
        continue
print()

number_of_drinkers = None
is_valid_number_of_drinkers = None
while is_valid_number_of_drinkers is not True:
    number_of_drinkers = input("Enter the number of drinkers: ")
    # validate that the number of drinkers is actually a number
    if number_of_drinkers.isnumeric() is not True:
        print(f"TypeError: Invalid Input! "
              f"Please only enter a number\n")
        continue
    # validation passed
    # convert number_of_drinkers to int
    number_of_drinkers = int(number_of_drinkers)
    # make sure number of drinkers is at least 1
    if number_of_drinkers < 1:
        print("ValueError: Number of drinkers MUST be a positive number\n")
        continue
    # passed all validations
    is_valid_number_of_drinkers = True
print()

offset = None
valid_offset = None
while valid_offset is not True:
    offset = input("Enter an offset: ")
    # handle negative offset
    if offset[0] == '-':
        # validate that the part after the minus sign is a number
        if offset[1::].isnumeric() is not True:
            print(f"ValueError: offset MUST be a number\n")
            continue
    # handle positive offset
    # validate that the input is a number
    elif offset.isnumeric() is not True:
        print(f"ValueError: offset MUST be a number\n")
        continue
    # all validations passed
    # convert offset to int
    valid_offset = True
    offset = int(offset)
print()

# create a (mutable) list containing all coffee types to use as a filter
filtered_coffee_types = list(coffee_types)
excluded_coffee_types = []

should_exclude = None
while True:
    should_exclude = input("Would you like to exclude any Coffee types from this Coffee run? (Y/N): ").strip().lower()
    # handle incompatible answer
    if should_exclude != 'y' and should_exclude != 'n':
        print(f"ValueError: Expected 'Y' or 'N'\n")
        continue
    # validation passed
    # get bool value of input answer
    should_exclude = True if should_exclude == 'y' else False
    break
print()

excluded_coffee_type = None
if should_exclude is True:
    print(f"Enter Coffee numbers one by one to exclude them from this Coffee run.\n"
          f"When you are finished, enter '$'.\n")
    while True:
        # make sure a value exists
        if excluded_coffee_type is not None:
            # convert excluded_coffee_type to int
            excluded_coffee_type = int(excluded_coffee_type)
            # validate that excluded_coffee_type is not index overflowing
            if (1 <= excluded_coffee_type <= 28) is not True:
                print(f"ValueError: Excluded Coffee type MUST be a number between 1 and 28\n")
                excluded_coffee_type = None
                continue
            # all validations passed
            # append coffee type to excluded types list
            excluded_coffee_types.append(excluded_coffee_type)
        # get input from user
        excluded_coffee_type = input("Enter a Coffee number to exclude: ")
        # handle exit character for continuing with the program
        if excluded_coffee_type == '$':
            break
        # validate the input is a number
        if excluded_coffee_type.isnumeric() is not True:
            print(f"TypeError: Expected int\n")
            excluded_coffee_type = None
            continue

# filter the coffee types
while len(excluded_coffee_types) > 0:
    # get the index to remove from the excluded list
    excluded_coffee = excluded_coffee_types[0]
    # get the name (type: str) of the coffee to remove
    coffee_type = coffee_types[excluded_coffee]
    # find the index of the excluded coffee in the filtered list
    coffee_pop_index = filtered_coffee_types.index(coffee_type)
    # remove excluded coffee from filter list
    filtered_coffee_types.pop(coffee_pop_index - 1)
    # remove current index from excluded list
    excluded_coffee_types.pop(0)

# the new length of the Coffee types
len_filter = len(filtered_coffee_types)

# calculate the coffee number for customer presentation
coffee_number = (hours + offset) % len_filter
# zero-index handling
coffee_type = filtered_coffee_types[coffee_number - 1]
print(f"\n******************************\n"
      f"User #1\n"
      f"Coffee #{coffee_types.index(coffee_type) + 1}: {coffee_type}")

# store the previous users coffee number to calculate other friends coffee number
previous_user_coffee = coffee_number
# iterate the rest of the drinkers
user = 2
while user <= number_of_drinkers:
    # calculate the coffee number for customer presentation
    coffee_number = (previous_user_coffee + minutes) % len_filter
    # zero-index handling
    coffee_type = filtered_coffee_types[coffee_number - 1]
    print(f"******************************\n"
          f"User #{user}\n"
          f"Coffee #{coffee_types.index(coffee_type) + 1}: {coffee_type}"
          )
    user += 1
    # update the previous coffee number
    previous_user_coffee = coffee_number
print("******************************")

print("""
 .---. .-. .-.  .--.  .-. .-..-. .-.   .-.  .-. .----. .-. .-.    
{_   _}| {_} | / {} \\ |  `| || |/ /     \\ \\/ / /  {}  \\| { } |    
  | |  | { } |/  /\\  \\| |\\  || |\\ \\      }  {  \\      /| {_} |    
  `-'  `-' `-'`-'  `-'`-' `-'`-' `-'     `--'   `----' `-----'    
         .----. .-.   .----.  .--.   .----..----.                 
         | {}  }| |   | {_   / {} \\ { {__  | {_                   
         | .--' | `--.| {__ /  /\\  \\.-._} }| {__                  
         `-'    `----'`----'`-'  `-'`----' `----'                 
 .---.  .----. .-.   .-..----.     .--.   .---.   .--.  .-..-. .-.
/  ___}/  {}  \\|  `.'  || {_      / {} \\ /   __} / {} \\ | ||  `| |
\\     }\\      /| |\\ /| || {__    /  /\\  \\  {_ }/  /\\  \\| || |\\  |
 `---'  `----' `-' ` `-'`----'   `-'  `-' `---' `-'  `-'`-'`-' `-'
""")
