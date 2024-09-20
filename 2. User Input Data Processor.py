# 2. User Input Data Processor, task 1: Input Length Validator
def check_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    if len(first_name) <= 1 or len(last_name) <= 1:
        print("Error: name should be longer than one character.")
    else:
        print("Your first name is", len(first_name), "characters long.")
        print("Your last name is", len(last_name), "characters long.")

check_name()