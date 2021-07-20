class dog():
    # 会自动运行init函数,初始化一个自身成员
    # self对实例自身的引用
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is  now sitting.")

    def roll_over(self):
        print(self.name.title() + "rolled over.")


my_dog = dog('willer', 6)
print(type(my_dog.name))
# title函数的意义是将字符串改为首字母大写
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
