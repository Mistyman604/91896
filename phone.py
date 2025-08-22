def phone(question, min, max):
    """Checks users enter an integer"""

    error = f"Please enter a number between {min} and {max} numbers long"

    while True:

        try:

            response = int(input(question))
            length = len(str(response))

            if min <= length <= max:
                return response
            elif length > max:
                print("Sorry, That isn't a legal phone number")
                print(error)
            elif length < min:
                print("Sorry, That isn't a legal phone number")
                print(error)
            else:
                print(error)

        except ValueError:
            print(error)


# get the users phone number
phone_number = phone("What is your phone number?    ", 8, 11)
print(phone_number)