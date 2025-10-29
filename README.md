# Calculator-CLI-App
# What I Built

I built a Command-Line Interface (CLI) Calculator using Python.
This calculator performs basic arithmetic operations — addition, subtraction, multiplication, and division — directly from the terminal.

It takes user input, processes calculations through defined functions, and displays results in real-time.
The program continues running until the user decides to exit, making it interactive and user-friendly.

# Why I Built It

The purpose of building this project was to:

Strengthen my understanding of Python fundamentals, including functions, loops, and conditional statements.

Practice user input handling and error management (e.g., invalid inputs, division by zero).

Learn how to structure a small, clean, and maintainable CLI-based Python application.

Fulfill the requirements of an internship/learning task focusing on Python scripting and problem-solving.

This project demonstrates the ability to build a real, working Python tool that interacts with users through the terminal.

# How I Built It
1. Planning

I started by identifying the basic operations needed:

- Addition

- Subtraction

- Multiplication

- Division

Then, I decided to implement each operation as a separate function for clean code organization.

2. Implementation

Created a Python script named calculator.py.

Defined functions: add(), subtract(), multiply(), and divide().

Added a main loop (while True) to continuously take user input until they type "exit".

Used the input() function for interaction and float() for numerical conversions.

- Implemented error handling for:

Non-numeric inputs (using try-except)

Division by zero (inside the divide() function)

Displayed results neatly after each operation.

3. Testing

Tested various cases to ensure:

Correct results for valid inputs

Proper handling of invalid data

Graceful program exit when "exit" is entered

- Example test:

Enter operation (+, -, *, /) or 'exit' to quit: +
Enter first number: 10
Enter second number: 5
Result: 15.0

# How to Run

Clone or download the project folder.

Open a terminal in the project directory.

Run the script with:

     python calculator.py


ies like colorama).

Package it as an installable Python module.
