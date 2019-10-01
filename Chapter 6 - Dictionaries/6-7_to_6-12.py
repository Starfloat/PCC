# 6-7

person1 = {'first_name':'bob',
           'last_name': 'billy',
           'age': 25,
           'city': 'greenville'
           }

person2 = {'first_name':'susan',
           'last_name':'kelly',
           'age':29,
           'city':'yellow city'
           }

person3 = {'first_name':'melanie',
           'last_name':'tran',
           'age':18,
           'city':'morelle'
           }

people = [person1, person2, person3]

for person in people:
    print('First Name: ' + person['first_name'].title())
    print('Last Name: ' + person['last_name'].title())
    print('Age: ' + str(person['age']))
    print('City: ' + person['city'].title()+"\n")

# 6-8

rascal = {'animal':'dog', 'owner':'bob'}
bella = {'animal':'dog', 'owner':'billy'}
wade = {'animal':'cat', 'owner':'susan'}

pets = [rascal, bella, wade]

for pet in pets:
    print('Owner: ' + pet['owner'].title())
    print('Pet: ' + pet['animal']+"\n")

# 6-9

favorite_places = {'bob':['paris','rome'],
                   'billy':['london'],
                   'mark':['maui','yosemite','barcelona']
                   }

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print("\t"+place.title())

# 6-10 (list in a dictionary)

favorite_number = {'bob':[1,6,9],
                    'alice':[42,32,5],
                    'mark':[63,69,28],
                    'eric':[74,4],
                    'hart':[24,7,8]
                    }
for name, numbers in favorite_number.items():
    print(name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print(str(number))

# 6-11 (dictionary in a dictionary)

cities = {
    'Charleston': {'Country':'united states',
                   'Population':130113,
                   'Fact':'Defined by its cobblestone streets, horse-drawn carriages and pastel antebellum houses.'},
    'Santa Fe': {'Country':'united states',
                 'Population':83776,
                 'Fact':"It's renowned for its Pueblo-style architecture and as a creative arts hotbed."},
    'New Orleans': {'Country':'united states',
                     'Population':393292,
                     'Fact':"Nicknamed the 'Big Easy', it's known for its round-the-clock nightlife, vibrant live-music scene and " +
                     "spicy, singular cuisine."}
    }

for city, information in cities.items():
    country = information['Country']
    population = information['Population']
    fact = information['Fact']
    
    print(city +
          "\n\tCountry: " + country.title() +
          "\n\tPopulation: " + str(population) +
          "\n\tFact: " + fact + "\n"
          )

# 6-12

users = {

'user_0':{
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    'favorite color':['yellow','red']
    },

'user_1':{
    'username': 'bbob',
    'first': 'billy',
    'last': 'bob',
    'favorite color':['blue', 'green']
    },

'user_2': {
    'username': 'sellen',
    'first': 'sue',
    'last': 'ellen',
    'favorite color':['black','white']
    },
}

# to do: get the value list to print in a loop

for user, userinfo in users.items():
    print('Username: ' + userinfo['username'])
    print('First Name: ' + userinfo['first'])
    print('Last Name: ' + userinfo['last'])
    for language in userinfo.values():
        print('Favorite language: ' + str(language))
    
