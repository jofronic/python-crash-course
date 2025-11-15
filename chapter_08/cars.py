def cars(manuf, make, **car_info):
    """This function stores information about a car"""
    car_info['Manufacturer'] = manuf
    car_info['Model'] = make
    return car_info
car_profile = cars('subaru', 'outback', color='blue', tow_package=True,)

print(car_profile)

