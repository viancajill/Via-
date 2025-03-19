# Import necessary modules
import math

# 1. Define the MathOperations class that uses multiple keywords
class MathOperations:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Method demonstrating 'if', 'elif', and 'else'
    def calculate(self):
        try:
            # Check if both numbers are positive, perform addition
            if self.x > 0 and self.y > 0:
                return self.x + self.y
            # If either is zero, return zero
            elif self.x == 0 or self.y == 0:
                return 0
            # Otherwise, return multiplication result
            else:
                return self.x * self.y
        except Exception as e:
            # Catch any exception that occurs
            print(f"Error: {e}")
        finally:
            # Ensures this block always runs after try/except
            print("Calculation attempt finished.")

    # Method demonstrating 'while' loop and 'break'
    def countdown(self):
        count = self.x
        while count > 0:
            print(count)
            count -= 1
            if count == 3:
                break  # Break the loop if count reaches 3
        else:
            print("Countdown completed!")

# 2. Helper function demonstrating 'lambda', 'return', and 'assert'
def square(x):
    # Lambda function to square a number
    return x ** 2

# 3. Another helper function demonstrating 'global', 'nonlocal', and 'del'
counter = 0  # Global variable

def increment_global():
    global counter  # Modify the global variable
    counter += 1
    print(f"Global counter: {counter}")

def outer_function():
    count = 0  # Local variable

    def inner_function():
        nonlocal count  # Access and modify the enclosing variable
        count += 1
        print(f"Inner function count: {count}")

    inner_function()  # Call inner function

# 4. Function demonstrating 'assert', 'del' and handling NameError
def assert_del_example():
    x = 10
    assert x > 0  # Assert x is positive
    print(f"x is {x}")
    del x  # Delete the variable x
    try:
        print(x)  # This will raise an error
    except NameError as e:
        print(f"Error: {e}")

# 5. File handling with 'with'
def write_file():
    with open("example.txt", "w") as f:
        f.write("Python keywords demonstration\n")  # Automatically closes file

# 6. Function demonstrating 'in', 'is', 'not', 'True', 'False'
def check_elements():
    my_list = [1, 2, 3, 4, 5]
    if 3 in my_list:  # Check membership using 'in'
        print("3 is in the list.")

    if 6 not in my_list:  # Check non-membership using 'not in'
        print("6 is not in the list.")

    if my_list[0] is 1:  # Check object identity with 'is'
        print("First element is 1.")
    
    print(True, False)  # Using boolean constants True and False

# 7. Function demonstrating 'pass' and 'continue'
def pass_continue_example():
    for i in range(5):
        if i == 2:
            pass  # Do nothing when i equals 2
        elif i == 4:
            continue  # Skip the iteration when i equals 4
        print(f"Value of i: {i}")

# 8. Main function to tie everything together
def main():
    # Create an instance of MathOperations and demonstrate keyword usage
    math_op = MathOperations(3, 4)
    print("Sum or Product:", math_op.calculate())  # Uses 'if', 'elif', 'else'

    # Countdown demonstration
    math_op.countdown()

    # Test square function with lambda
    print("Square of 5:", square(5))

    # Demonstrating global and nonlocal usage
    increment_global()
    outer_function()

    # Using 'assert' and 'del'
    assert_del_example()

    # Write to file using 'with'
    write_file()

    # Check elements in a list using 'in', 'is', and boolean values
    check_elements()

    # Pass and continue example
    pass_continue_example()

# 9. Entry point for the program
if __name__ == "__main__":
    main()  # Execute the main function
