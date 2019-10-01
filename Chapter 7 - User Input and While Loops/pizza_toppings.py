# 7-4

while True:
    topping = print('What topping would you like for your pizza? ')
    topping = input("Type 'quit' to exit: \n")

    if topping == 'quit':
        break
    else:   
        print('Adding ' + topping + (' to your pizza.'))
