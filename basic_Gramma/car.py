class Car():
    def __init__(self, make, mode, year):
        self.make = make
        self.mode = mode
        self.year = year
        # 设置初始值之后，无需包含为其提供初始值的形参
        self.odmeter_reading = 0

    def get_discriptable_infor(self):
        long_name = str(self.year) + ' '+self.make + ' ' + self.mode
        return long_name.title()

    def read_odmeter(self):
        print("This car has "+str(self.odmeter_reading)+' miles on it.')

    def update_odmeter(self, mileage):
        if mileage > self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("禁止回调")

    def increment_odmeter(self, miles):
        if miles >= 0:
            self.odmeter_reading += miles
        else:
            print("禁止回调")


'''
    继承将获得父类的所有属性和方法
'''


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def decribe_battery(self):  # 再定义子类方法，父类无法使用
        '''打印一条描述电池容量的消息'''
        print("This car has a " + str(self.battery_size)+"-kwh batter.")
    
    def get_range(self):
        '''打印一条电池的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 80:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectriCar(Car):
    def __init__(self, make, mode, year):
        '''
            初始化父类的属性
        '''
        super().__init__(make, mode, year)
        self.battery = Battery()



