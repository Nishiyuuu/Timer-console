import time
print("Hello i am timer:)\nPlease write me a clock minutes and seconds:")
hour = 0
minute = 0
second = 0
while True:
    try:
        hour = int(input("Hours: "))
        minute = int(input("Minutes: "))
        second = int(input("Seconds: "))
        break
    except ValueError:
        print("Please write a number!")
        continue
while True:
    if (second > 60):
        minute += second // 60
        second %= 60
    if (minute > 60):
        hour += minute // 60
        minute %= 60
    if hour == 0 and minute == 0 and second == 0:
        print("Time is over!")
        break
    print(f"{hour}:{minute}:{second}")
    time.sleep(1)
    second -= 1
    if second < 0:
        second = 59
        minute -= 1
    if minute < 0:
        minute = 59
        hour -= 1
    if hour < 0:
        hour = 0