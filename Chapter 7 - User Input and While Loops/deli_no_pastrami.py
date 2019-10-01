sandwich_orders = ['pastrami', 'cheesesteak', 'french dip', 'pastrami', 'blt', 'lobster roll', 'gyro', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        print('Sorry, we ran out of Pastrami.')
    else:
        print("I made your " + sandwich.title() + ".")
        finished_sandwiches.append(sandwich)
