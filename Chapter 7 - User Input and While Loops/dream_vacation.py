dream_vacation_responses = {}

polling_active = True

while polling_active:
    # Prompt
    name = input("Enter your name: \n")
    response = input("If you could visit one place in the world, where would you go?\n")

    # Store the response in the dictionary
    dream_vacation_responses[name] = response
    
    # Find out if anyone else would like to take the poll.
    repeat = input("Is there another person who would like to take the poll? (yes/no)\n")
    if repeat == 'no':
        polling_active = False

    for name, response in dream_vacation_responses.items():
        print(name.title() + "'s dream vacation is " + response + ".") 
    
