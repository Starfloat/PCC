def make_sandwich(*toppings):
    print('\nMaking sandwich which has:')
    for topping in toppings:
        print('- ' + topping)

make_sandwich('lettuce', 'bacon', 'tomato')
make_sandwich('cheese', 'steak')
make_sandwich('meatball', 'pepperoni')
