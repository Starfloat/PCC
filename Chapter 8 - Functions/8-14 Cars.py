def car_info(manufacturer, model, **other_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in other_info.items():
        car[key] = value
    return car

car = car_info('ACURA', 'TSX',
               year=2006,
               color='blue')
print(car)
