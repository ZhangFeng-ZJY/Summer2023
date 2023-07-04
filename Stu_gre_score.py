# 导入tkinter库
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import *
import time

"""
    欢迎页面
"""


def win_usu_log():
    global win_usu_login
    win_usu_login = Tk()
    win_usu_login.title('欢迎来到南传成绩查询！')
    win_usu_login.geometry('350x150+500+300')
    Label(win_usu_login, text='账号:').place(x=50, y=30)
    uname = Entry(win_usu_login)
    uname.place(x=100, y=30)
    # 设置密码
    Label(win_usu_login, text='密码:').place(x=50, y=70)
    pwd = Entry(win_usu_login)
    pwd.place(x=100, y=70)

    Button(win_usu_login, text='登陆').place(x=100, y=110)
    Button(win_usu_login, text='返回上一级').place(x=170, y=110)
    win_usu_login.mainloop()

    # 登陆
    def login():
        global username, password, flag
        username = uname.get()
        password = pwd.get()
        flag = 1
        time.sleep(1)
        if_enter()

    def re():
        win_usu_login.destroy()
        first()

    # 登陆按钮
    Button(win_usu_login, text='登陆', command=login).place(x=100, y=110)
    Button(win_usu_login, text='返回上一级', command=re).place(x=170, y=110)

    win_usu_login.mainloop()


def win_gre_log():
    global win_gre_login
    win_gre_login = Tk()
    win_gre_login.title('欢迎来到南传成绩管理！')
    win_gre_login.geometry('350x150+500+300')
    Label(win_gre_login, text='账号:').place(x=50, y=30)
    uname = Entry(win_gre_login)
    uname.place(x=100, y=30)
    # 设置密码
    Label(win_gre_login, text='密码:').place(x=50, y=70)
    pwd = Entry(win_gre_login)
    pwd.place(x=100, y=70)

    # 登陆
    def login():
        global username, password, flag
        username = uname.get()
        password = pwd.get()
        flag = 2
        time.sleep(1)
        if_enter()

    def re():
        win_gre_login.destroy()
        first()

    # 登陆按钮
    Button(win_gre_login, text='登陆', command=login).place(x=100, y=110)
    Button(win_gre_login, text='反回上一级', command=re).place(x=170, y=110)

    win_gre_login.mainloop()


def go_usu_login():
    winHello.destroy()
    win_usu_log()


def go_ger_login():
    winHello.destroy()
    win_gre_log()


def go_win_set_gre():
    win_set_gre = Tk()
    win_set_gre.title('请设置账号密码')
    win_set_gre.geometry('350x150+500+300')
    Label(win_set_gre, text='账号:').place(x=50, y=30)
    uname = Entry(win_set_gre)
    uname.place(x=100, y=30)
    # 设置密码
    Label(win_set_gre, text='密码:').place(x=50, y=70)
    pwd = Entry(win_set_gre)
    pwd.place(x=100, y=70)

    def confirm():
        global gre_name, gre_pwd
        gre_name = uname.get()
        gre_pwd = pwd.get()
        time.sleep(1)
        win_set_gre.destroy()
        winHello.destroy()
        time.sleep(1)
        first()

    Button(win_set_gre, text='确定', command=confirm).place(x=50, y=100)
    win_set_gre.mainloop()


def first():
    global winHello
    winHello = Tk()
    winHello.title('你好！')
    winHello.geometry('350x150+500+300')
    Label(winHello, text='请选择普通登录与管理员登录！').place(x=80, y=75)
    Button(winHello, text='普通', command=go_usu_login).place(x=100, y=50)
    Button(winHello, text='管理员', command=go_ger_login).place(x=175, y=50)
    Button(winHello, text='创建管理员', command=go_win_set_gre).place(x=150, y=100)

    winHello.mainloop()


def login_use(une, pwd):
    if username == une:
        if password == pwd:
            return True
    else:
        return False


def longin_gre(une, pwd):
    if gre_name == une:
        if gre_pwd == pwd:
            return True
    else:
        return False


# 取消学生创建
def cancel_set_stu():
    win_student.destroy()
    win_gre_ent()


# 消息提示信息已经录入
"""def set_stu_mes_success():
    window = tkinter.Tk()
    window.withdraw()  # 退出默认 tk 窗口
    result = showinfo('提示', '这是一个提示框')
    print(f'提示: {result}')
"""


# 确定学生信息
def sure_set_stu():
    global all_student_list
    all_student_list.append(sin_stu)
    stu_amo()
    win_student.destroy()
    root = tkinter.Tk()
    root.withdraw()
    tkinter.messagebox.showinfo('提示', '你的输入有误')
    win_gre_ent()

# 判断现在存储学生人数
def stu_amo():
    global amount
    amount = len(all_student_list)


"""
    管理员存储方法
"""


def new_student():
    global win_student
    win_gre_enter.destroy()
    win_student = Tk()
    win_student.title('请输入学生各项信息！')
    win_student.geometry('350x350+500+200')
    Label(win_student, text='学号：').place(x=50, y=25)
    stu_inm_0 = Entry(win_student)
    stu_inm_0.place(x=125, y=25)
    Label(win_student, text='姓名：').place(x=50, y=50)
    stu_inm_1 = Entry(win_student)
    stu_inm_1.place(x=125, y=50)
    Label(win_student, text='课程代码:').place(x=50, y=75)
    stu_inm_2 = Entry(win_student)
    stu_inm_2.place(x=125, y=75)
    Label(win_student, text='课程名称:').place(x=50, y=100)
    stu_inm_3 = Entry(win_student)
    stu_inm_3.place(x=125, y=100)
    Label(win_student, text='课程性质:').place(x=50, y=125)
    stu_inm_4 = Entry(win_student)
    stu_inm_4.place(x=125, y=125)
    Label(win_student, text='学分:').place(x=50, y=150)
    stu_inm_5 = Entry(win_student)
    stu_inm_5.place(x=125, y=150)
    Label(win_student, text='成绩:').place(x=50, y=175)
    stu_inm_6 = Entry(win_student)
    stu_inm_6.place(x=125, y=175)
    Label(win_student, text='绩点:').place(x=50, y=200)
    stu_inm_7 = Entry(win_student)
    stu_inm_7.place(x=125, y=200)
    Label(win_student, text='任课老师:').place(x=50, y=225)
    stu_inm_8 = Entry(win_student)
    stu_inm_8.place(x=125, y=225)
    Label(win_student, text='是否挂科:').place(x=50, y=250)
    stu_inm_9 = Entry(win_student)
    stu_inm_9.place(x=125, y=250)

    def sure():
        global sin_stu
        sin_stu = [stu_inm_0.get(), stu_inm_1.get(), stu_inm_2.get(), stu_inm_3.get(), stu_inm_4.get(), stu_inm_5.get(),
                   stu_inm_6.get(), stu_inm_7.get(), stu_inm_8.get(), stu_inm_9.get()]
        sure_set_stu()

    Button(win_student, text='取消创建', command=cancel_set_stu).place(x=50, y=300)
    Button(win_student, text='确定', command=sure).place(x=150, y=300)
    win_student.mainloop()


def delete_student():
    pass



def add_student_grades():
    pass


def revise_student_grades():
    pass


""""""


def re_usu_log():
    win_usu_enter.destroy()
    win_usu_log()


def re_gre_log():
    win_gre_enter.destroy()
    win_gre_log()


# 普通用户界面
def win_usu_ent():
    global win_usu_enter
    win_usu_enter = Tk()
    win_usu_enter.title("欢迎来到学生成绩查询界面！")
    win_usu_enter.geometry('350x150+500+300')
    Button(win_usu_enter, text='返回上一级', command=re_usu_log).place(x=80, y=50)
    Button(win_usu_enter, text='查询成绩', command=delete_student).place(x=80, y=75)
    win_usu_enter.mainloop()


# 管理员界面
def win_gre_ent():
    global win_gre_enter
    win_gre_enter = Tk()
    win_gre_enter.title("欢迎来到管理员界面！")
    win_gre_enter.geometry('350x150+500+300')
    Button(win_gre_enter, text='返回上一级', command=re_gre_log).place(x=80, y=25)
    Button(win_gre_enter, text='新建学生', command=new_student).place(x=80, y=50)
    Button(win_gre_enter, text='删除学生', command=delete_student).place(x=80, y=75)
    Button(win_gre_enter, text='添加学生成绩', command=add_student_grades).place(x=80, y=100)
    Button(win_gre_enter, text='修改学生成绩', command=revise_student_grades).place(x=80, y=125)
    win_gre_enter.mainloop()


def use_enter():
    win_usu_login.destroy()
    win_usu_ent()


def gre_enter():
    win_gre_login.destroy()
    win_gre_ent()


def if_enter():
    if flag == 1:
        if login_use(username, password):
            use_enter()
        else:
            print("no1")  # 用户名或密码错误
    if flag == 2:
        if longin_gre(username, password):
            gre_enter()
        else:
            print("no2")  # 用户名或密码错误


if __name__ == '__main__':
    all_student_list = []
    """
    [
    [学号] 0
    [name] 1    
    [课程代码] 2
    [课程名称] 3
    [课程性质] 4
    [学分] 5
    [成绩] 6
    [绩点] 7
    [任课老师] 8
    [是否挂科] 9
    ]
    """

    # 普通用户
    username = ''
    password = ''

    # 管理员
    gre_name = ''
    gre_pwd = ''
    flag = 0  # 1为普通 2 为管理员

    first()
