print("🎲🎲 roll it 13 🎲🎲")

# looping for testing purposes
while True:
    want_instructions = input("Do you want to read the instructions?").lower()

    if want_instructions == "yes":
        print("you chose yes")
    elif want_instructions == "no":
        print("you chose no")
    else:
        print("you did not choose a valid response")

