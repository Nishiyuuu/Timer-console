import time
print("Hello i am timer:)\nPlease write me a clock minutes and seconds:")
a = int(1)
while(a > 0):
    clock = int(input("Clock:"))
    minutes = int(input("Minutes"))
    seconds = int(input("Seconds"))
    if (clock > 0 and minutes > 0 and seconds > 0):
        a = 0
    else:
        print("Please write me a correct clock minutes and seconds")
        a = 1
print("Timer is starting...")
while(clock > 0):
    while(minutes > 0):
        while(seconds > 0):
            time.sleep(1)
            print(clock, ":", minutes, ":", seconds)
            seconds -= 1
        minutes -= 1
        seconds = 59
    clock -= 1
    minutes = 59
    seconds = 59
    
    
