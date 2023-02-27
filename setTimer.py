import time


timer = input('Please insert time to count down (h:m:s or in seconds): ')

def countdown(setTime):
    for i in range(setTime, -1, -1):
        sec = i % 60
        min = int(i / 60) % 60
        hour = int(i / 3600)
        time.sleep(1)
        print(f"{hour:02}:{min:02}:{sec:02}")


if ":" in timer:
    hour, min, sec = timer.split(':')
    setTime = int(hour) * 3600 + int(min) * 60 + int(sec)
    countdown(setTime)
elif timer:
    countdown(int(timer))

print("Your time is over !")
