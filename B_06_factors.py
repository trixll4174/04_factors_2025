# generates headings (e.g., ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "-")
    print('''
    To use this program simply enter an integer between 1 and 200.
    The program will show the factors of your chosen integer.

    It will also tell you if your chosen integer...
      - is a prime number (i.e: it has 2 factors)
      - is a perfect square

    To exit the program, type 'xxx'
        ''')


# Ask the user for width and loop until they enter a number between 1 and 200
def int_check(question):
    error = f"Please enter a whole number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = int(response)
            if 1 <= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Function to find all factors of a given number
def factor_finder(var_to_factor):
    factor = []

    for i in range(1, var_to_factor + 1):
        if var_to_factor % i == 0:
            factor.append(i)

    return factor


# Main routine goes here
statement_generator("The Ultimate Factor Finder", "-")

# Ask if the user wants to see instructions and only show them once
want_instructions = input("\nPress <enter> to read the instructions or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    to_factor = int_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    all_factors = factor_finder(to_factor)

    if to_factor == 1:
        comment = "One is UNITY. It only has one factor: itself :)"

    elif len(all_factors) == 2:  # Check for prime number (only two factors)
        comment = f"{to_factor} is a prime number"

    elif len(all_factors) % 2 == 1:  # Check for perfect square (odd number of factors)
        comment = f"{to_factor} is a perfect square"

    # Print the results
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factor calculator ;) ")