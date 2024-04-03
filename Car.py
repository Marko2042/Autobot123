import json
from car.car_price import cars
def keyb_price():
    with open('C:/Users/WellDone/PycharmProjects/pythonProject4/car/car.json') as _:
        data = json.load(_)
        key_price = data.keys()
        print(key_price)
    return key_price

def car_1000():
    global cars
    car = cars["Car 1000$"]
    brand = []
    for i in car:
        brand.append(i["brend"])
    return brand

def Car_info(info,index):
    global cars
    car = cars[info][index]
    return car

def car_5000():
    global cars
    car = cars["Car 5000$"]
    brand = []
    for i in car:
        brand.append(i["brend"])
    return brand

def car_10000():
    global cars
    car = cars["Car 10000$"]
    brand = []
    for i in car:
        brand.append(i["brend"])
    return brand

def car_50000():
    global cars
    car = cars["Car 50000$"]
    brand = []
    for i in car:
        brand.append(i["brend"])
    return brand
