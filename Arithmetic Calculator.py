def main():
    # Ask user to choose an arithmetic operation
    print("Please pick an arithmetic.")
    print("addition")
    print("subtraction")
    print("multiplication")
    print("division")
    
    # Read the chosen operation
    math = input().lower()
    
    # Ask for two numbers
    print("Now please input a first number.")
    one = float(input())
    
    print("Now please input a second number.")
    two = float(input())
    
    # Initialize result and operation name
    result = 0
    operation = ""
    
    # Perform the operation based on user input
    if math == "addition":
        print("You picked Addition.")
        result = one + two
        operation = "sum"
    elif math == "subtraction":
        print("You picked Subtraction.")
        result = one - two
        operation = "difference"
    elif math == "multiplication":
        print("You picked Multiplication.")
        result = one * two
        operation = "product"
    elif math == "division":
        print("You picked Division.")
        if two != 0:  # Prevent division by zero
            result = one / two
            operation = "quotient"
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("That is not an arithmetic operation.")
        return
    
    # Round the result to 2 decimal places
    result = round(result, 2)
    
    # Output the result
    print(f"The {operation} of {one} and {two} is equal to {result}")

# Run the main function
if __name__ == "__main__":
    main()
    # NOTE: THIS CODE WAS WRITTEN IN C# AND CONVERTED TO PYTHON USING CHATGPT