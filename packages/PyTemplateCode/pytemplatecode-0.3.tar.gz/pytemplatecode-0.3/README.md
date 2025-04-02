# PyTemplateCode

This is a simple Python template project for beginners. It includes some useful functions, including a timer, current time fetcher, input validation, and simple decorative print functions.

## GitHub Repository!

All code you can find the source code and contribute to the project on [GitHub](https://github.com/KusokMedi/pytemplatecode).

## Installation

You can install this package via `pip`:

```
pip install pytemplatecode
```

## Functions List

1. timer(seconds)
2. current_time(format="%Y-%m-%d %H:%M:%S")
3. inputint(prompt="Enter a number: ")
4. start(name="Your project name", delay=0.25)
5. end(end_text="End of code!", delay=0.25)
6. crash(seconds=0)
7. printedit(*args)

## Functions

### 1. `timer(seconds)`
Counts down from the specified number of seconds and prints the remaining time every second.

- `seconds` (int): The number of seconds to count down.
- Raises a `ValueError` if the input is not an integer.

### 2. `current_time(format="%Y-%m-%d %H:%M:%S")`
Returns the current time formatted according to the specified format.

- `format` (str): The format in which to return the current time. Default is "%Y-%m-%d %H:%M:%S".

### 3. `inputint(prompt="Enter a number: ")`
Prompts the user to enter a valid integer and returns it. If the user enters a non-integer value, an error message is displayed.

- `prompt` (str): The prompt message displayed to the user.

### 4. `start(name="Your project name", delay=0.25)`
Displays a decorated banner at the beginning of the program with customizable text and delay time.

- `name` (str): The name of your project that will be displayed in the banner.
- `delay` (float): The delay in seconds between each character printed.

### 5. `end(end_text="End of code!", delay=0.25)`
Prints an end message with a decorated banner.

- `end_text` (str): The message to display at the end.
- `delay` (float): The delay in seconds between each character printed.

### 6. `crash(seconds=0)`
Simulates a crash after a specified number of seconds with a countdown and "CRASHED" message.

- `seconds` (int or float): The number of seconds until the crash.
- Raises a `ValueError` if seconds is negative or not a valid number.

### 7. `printedit(*args)`
Dynamically updates the printed text in the same line, displaying elements sequentially. If any error occurs, prints corresponding error message and continues.

- First argument (optional) - text color (str).
- Remaining arguments - alternating list of text (str) and delay (float).

### Colors:

- 🔴 Red  
- 🟢 Green  
- 🟡 Yellow  
- 🔵 Blue  
- 🟣 Magenta  
- 🔵 Cyan  
- ⚪ White  
- ❌ Reset  

## Usage

Here is a quick example of how you can use the functions in this package:

```python
from pytemplatecode import *
from time import sleep

# Start the project with a cool banner
start(name="My Project + PyTemplateCode")

sleep(0.25)

# Display current time
print(f"Current time is: {current_time()}")

# Prompt user for an integer
number = inputint("Enter a number: ")

print(f"Fine, You entered: {number}, and its very eazy to take number corectly!")

# Countdown timer
timer(5)

# End the project with a banner
end(end_text="Project Completed!")

# Simulate a crash (deleate line 97 to cool dialog :3)
crash(5)

# Code didn't work :0
print("Human: What the hell?")
input("\nPress enter to continue\n")
print("You: Hell the what..")
```
