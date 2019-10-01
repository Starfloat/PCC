# 7-1

rental_car = input("What kind of rental car would you like? ")
print("Let me see if I can find you a " + rental_car.title() + ".")


# 7-2

num_of_people = int(input("How many people are in your dinner group? "))
if num_of_people > 8:
    print("You'll have to wait for a table.")
else:
    print("You have a table ready.")

# 7-3

number = int(input("Enter a number: "))
if number % 10 == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")
