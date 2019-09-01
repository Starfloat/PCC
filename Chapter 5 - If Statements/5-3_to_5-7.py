# 5-3
alien_color = 'green'

if alien_color == 'green':
    print('You have earned 5 points.')

if alien_color == 'yellow':
    print('You have earned 5 points.')

# 5-4
alien_color = 'yellow'

if alien_color != 'green':
    print('You have earned 10 points')

if alien_color == 'green':
    print('You have earned 5 points.')
else:
    print('You have earned 10 points.')

# 5-5

if alien_color == 'green':
    print('You have earned 5 points.')
elif alien_color == 'yellow':
    print('You have earned 10 points.')
elif alien_color == 'red':
    print('You have earned 15 points.')

# 5-6

age = 66
if age < 2:
    print('You are a baby.')
elif age >= 2 and age < 4:
    print('You are a toddler.')
elif age >= 4 and age < 13:
    print('You are a kid.')
elif age >= 13 and age < 20:
    print('You are a teenager.')
elif age >= 20 and age < 65:
    print('You are an adult.')
elif age > 65:
    print('You are an elder.')


# 5-7

favorite_fruits = ['apple', 'orange', 'banana']
if apple in favorite_fruits:
    print('You really like apples!')
if orange in favorite_fruits:
    print('You really like oranges!')
if peach in favorite_fruits:
    print('You really like peaches!')

