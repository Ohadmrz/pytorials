import time

seconds = int(input("Insert seconds: "))

while seconds > 0:
    print(f"{round(seconds, 1)} seconds left")
    time.sleep(0.1)
    seconds -= 0.1
print("DONE")