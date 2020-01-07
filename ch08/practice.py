def make_car(name, type, **other_info):
    car = {"name": name, "type": type}
    for key, value in other_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)