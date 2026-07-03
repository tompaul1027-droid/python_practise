# Task: Create a function called double_number that takes a number as an input.

# Action: Multiply that number by 2. Instead of printing it, return the result.

# The Test: Save the result of the function to a variable called result and then print that variable.

# Analogy: A vending machine doesn't just show you the soda; it gives it to you so you can take it home.


def double_number(a):
    return a*2


a=int(input("Enter the number:"))
result= double_number(a)
print(result)
