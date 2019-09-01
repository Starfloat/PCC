# 4-10

pets = ['cat', 'dog', 'fish', 'bunny', 'bird', 'hamster', 'turtle']

print('The first three items in this list are: ' + str(pets[:3]))
print('Three items from the middle of the list are: ' + str(pets[2:-2]))
print('The last three items in the list are: ' +str(pets[-3:]))

# 4-11

my_pizza_topping = ['spinach','mushroom','garlic']
friends_pizza_topping = my_pizza_topping[:]
my_pizza_topping.append('sausage')
friends_pizza_topping.append('pepperoni')
print(my_pizza_topping)
print(friends_pizza_topping)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)
