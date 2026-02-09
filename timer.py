import time

text = input("Insert time to count down (h:m:s): ")

text = text.split(":")
timer = [int(text[0]), int(text[1]), int(text[2]),]
seconds = timer[0]*3600 + timer[1]*60 + timer[2]

print(seconds)

start_time = time.time()
current_time = start_time
while (current_time - start_time) < seconds:
    current_time = time.time()
    print(f"{timer}")
    timer[2] -= 1
    if timer[2] == -1 and timer[1] != 0:
        timer[2] = 59
        timer[1] -= 1
        if timer[1] == -1 and timer[0] != 0:
            timer[1] = 59
            timer[0] -= 1


    time.sleep(1)