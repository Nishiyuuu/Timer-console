# Countdown Timer

This is a simple Python script that acts as a countdown timer.

## How it works

The script uses three nested while loops to count down the hours (clock), minutes, and seconds. The outermost loop represents the hours, the next one represents the minutes, and the innermost loop represents the seconds.

Each second, the script sleeps for one second using the `time.sleep(1)` function, then prints the current time left in the format `hours : minutes : seconds`. After printing, it decrements the seconds by one.

When the seconds reach 0, the minutes are decremented by one and the seconds are reset to 59. Similarly, when the minutes reach 0, the hours are decremented by one and both the minutes and seconds are reset to 59.

## Code Explanation

The code provided is a simple countdown timer implemented in Python. It uses three nested while loops to count down the hours (referred to as `clock` in the code), minutes, and seconds. 

Here's a brief explanation of the code:

- The outermost loop represents the hours. As long as `clock` is greater than 0, the loop will continue.
- The next loop represents the minutes. As long as `minutes` is greater than 0, the loop will continue.
- The innermost loop represents the seconds. As long as `seconds` is greater than 0, the loop will continue.
- Inside the innermost loop, the script sleeps for one second using the `time.sleep(1)` function, then prints the current time left in the format `hours : minutes : seconds`. After printing, it decrements the seconds by one.
- When the seconds reach 0, the minutes are decremented by one and the seconds are reset to 59.
- Similarly, when the minutes reach 0, the hours are decremented by one and both the minutes and seconds are reset to 59.

## Usage

To use this script, simply run it in your Python environment. You will need to set the initial values of `clock`, `minutes`, and `seconds` to the desired countdown time before running the script.