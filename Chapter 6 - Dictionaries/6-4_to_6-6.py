# 6-4

favorite_number = {'bob':1,
                    'alice':42,
                    'mark':63,
                    'eric':74,
                    'hart':24
                    }

for name, number in favorite_number.items():
    print(name.title() + "'s " + "favorite number is " + str(number) + ".")

# 6-5
print('\n')
rivers = {'nile':'egypt',
          'mississippi':'united states of america',
          'volga':'russia',
          }
          
for river, country in rivers.items():
    print(river.title() + " runs in " + country.title())

print('\n')
for river in rivers.keys():
    print(river.title())

for name in rivers.values():
    print(name.title())

# 6-6
print('\n')
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }

poll_list = ['bob','jen','billy','pam']

for name in poll_list:
    if name in favorite_languages:
        print('Thank you, ' + name.title() + ' for taking the poll.')
    else:
        print(name.title() + ', please take the poll.')

