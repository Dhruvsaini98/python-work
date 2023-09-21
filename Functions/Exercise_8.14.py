def car(manufacturer, model, **additional):
    additional['Manufacturer'] = manufacturer
    additional['Model'] = model
    return additional

car_details = car('Maruti Suzuki', 'Swift', color = 'Black', type = 'CNG', spoiler = 'Yes')
print(car_details)