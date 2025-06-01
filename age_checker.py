
age_input = input("Please enter your age: ")


if age_input.isdigit():
    age = int(age_input)
    if 10 <= age <= 20:
        print("Your age is between 10 and 20.")
    else:
        print("Your age is not between 10 and 20.")
else:
    print("Invalid input. Please enter a numeric value for age.")
