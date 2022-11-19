time = input("time of order (4 numbers): ")
time = time.strip()
num_of_friends = int(input("how many friends will you order the coffee with? "))
hours = time[0:2:1]
minutes = time[2:4:1]

coffee_types = ["espresso", "doppio", "lungo", "ristretto", "macchiato", "corretto", "con panna", "romano",
                "cappuccino", "americano", "cafe latte", "flat white", "marocchino", "mocha", "bicerin",
                "breve", "raf coffee", "mead raf", "vienna coffee", "chocolate milk", "latte macchiato", "glace",
                "freddo", "irish coffee", "frappe", "cappuccino freddo", "caramel frappe", "espresso laccino"]
if(int(hours)>23 or int(hours) < 0 or int(minutes) > 59 or int(minutes) < 0 or len(time) > 4 or len(time) < 0):
    print("invalid time")
else:
    print("you should drink: ", coffee_types[int(hours)])
    while(num_of_friends > 0):
        friend_drink_choice = int(hours)+int(minutes)num_of_friends
        if(int(hours)+int(minutes)num_of_friends > 28):
            friend_drink_choice = int(hours)+int(minutes)*num_of_friends % 28
        print("friend #", num_of_friends, "should drink: ", coffee_types[friend_drink_choice])
        num_of_friends -= 1