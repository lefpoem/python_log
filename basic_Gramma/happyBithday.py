'''
    通过此程序试验自定义函数
'''
def happy():
    print("Happy birthday to you!")
def happyB(name):
    happy()
    happy()
    print("Happy birthday, Dear {}!".format(name))
    happy()
happyB("Mike")
happy()
happyB("Lisa")