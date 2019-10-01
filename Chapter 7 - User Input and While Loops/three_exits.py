# 7-6

# Flag to exit
active = True

while active:
    topping = print('What topping would you like for your pizza? ')
    topping = input("Type 'quit' to exit: \n")

    if topping == 'quit':
        active = False

    else:
        print("Adding " + topping + ' to your pizza.\n')


# incrementor exit
prompt = print('You may only have 5 toppings on your pizza.')
prompt = print('What topping would you like for your pizza? ')
topping_count = 0
while topping_count < 5:
    topping = input()
    topping_count += 1
    print("Adding " + topping + " to your pizza.")
    if topping_count < 5:
        print(str(topping_count) +"/5 of topping used.")
        print('Add another topping: ')


