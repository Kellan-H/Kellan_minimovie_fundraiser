
valid_input = False
while valid_input == False:
    want_instructions = input("Do you want to read the instructions? ").lower()
    if want_instructions == "yes":
        print("instructions go here")
        valid_input = True
    elif want_instructions == "no":
        valid_input = True
        pass
    else:
        print("please enter yes or no")
        valid_input = False