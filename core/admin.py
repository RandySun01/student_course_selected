from lib import common
from interface import admin_interface, common_interface

"""
@author RansySun
@create 2019-08-31-15:31
"""
admin_info = {'user': None}


def register():
    """
    注册信息
    """
    username, pwd = common.input_username_pwd()
    flag, msg = admin_interface.register_interface(username, pwd)

    if flag:
        print(msg)
    else:
        print(msg)


def login():
    """
    登录
    """
    username, pwd = common.input_username_pwd()
    flag, msg = admin_interface.login_interface(username, pwd)

    if flag:
        print(msg)
        admin_info['user'] = username
    else:
        print(msg)

@common.lagoin_auth("admin")
def create_school():
    """
    创建学校
    """
    school_name = input("请输入学校名称")
    school_addr = input("请输入学校地址")

    flag, msg = admin_interface.create_school_interface(admin_info.get('user'), school_name, school_addr)

    if flag:
        print(msg)
    else:
        print(msg)

@common.lagoin_auth("admin")
def create_teacher():
    """
    创建老师
    """
    teacher_name = input("请输入老师姓名")
    flag, msg = admin_interface.create_teacher_interface(admin_info.get('user'), teacher_name)

    if flag:
        print(msg)
    else:
        print(msg)

@common.lagoin_auth("admin")
def create_course():
    """
    创建课程
    """
    while True:
        # 1获取学校列表
        school_list = common_interface.get_school_list()

        if not school_list:
            print("学校不存在")

        # 2打印学校列表
        for inex, school in enumerate(school_list):
            print(inex, school)

        # 3 选择学校
        choise = input("请输入学校编号")
        if choise == 'q':
            break

        if not choise.isdigit():
            print("学校不存在")
            continue

        choise = int(choise)
        if choise not in range(len(school_list)):
            print("学校不存在")
            continue
        # 3 逻辑判断
        school_name = school_list[choise]
        course_name = input("请输入课程名称")

        flag, msg = admin_interface.create_course_interface(admin_info.get('user'), school_name, course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


func_dic = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course,
}


def admin_view():
    while True:
        print('''
        1.注册
        2.登录
        3.创建学校
        4.创建老师
        5.创建课程
        q.退出
        ''')

        choice = input("请输入功能视图")
        if choice == 'q':
            break

        if choice not in func_dic:
            print("输入错误")
            continue

        func_dic.get(choice)()
