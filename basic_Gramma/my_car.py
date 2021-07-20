from car import *
my_tesla = ElectriCar('tesla', 'model s', '2016')
my_new_car = Car("audi", "a4", 2016)
my_new_car.odmeter_reading = 10000  # 直接修改属性值
my_new_car.update_odmeter(20000)  # 调用方法修改属性值
my_new_car.increment_odmeter(100)  # 通过方法对属性值进行递增
print(my_new_car.get_discriptable_infor())
print(my_new_car.read_odmeter())
print(my_tesla.get_discriptable_infor())

# battery是一个Battery类对象,同时也是ElectricCar的属性
my_tesla.battery.decribe_battery()  # 方法里有pirnt，不允许再使用print
my_tesla.battery.get_range()