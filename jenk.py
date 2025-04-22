import sys
 
# Accepting two arguments from command line

if len(sys.argv) != 3:

    print("Usage: python add.py <num1> <num2>")

    sys.exit(1)
 
try:

    num1 = float(sys.argv[1])

    num2 = float(sys.argv[2])

    result = num1 + num2

    print(f"The sum of {num1} and {num2} is {result}")

except ValueError:

    print("Please provide valid numbers.")

    sys.exit(1)

 
