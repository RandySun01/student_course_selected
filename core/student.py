from lib import common
from interface import student_interface, common_interface

"""
@author RansySun
@create 2019-08-31-15:31
"""
student_info = {'user': None}


def register():
    """
    注册信息
    """
    username, pwd = common.input_username_pwd()
    flag, msg = student_interface.register_interface(username, pwd)

    if flag:
        print(msg)

    else:
        print(msg)


def login():
    """
    学生登录接口
    """
    username, pwd = common.input_username_pwd()
    flag, msg = student_interface.login_interface(username, pwd)

    if flag:
        print(msg)
        student_info['user'] = username
    else:
        print(msg)


@common.lagoin_auth('student')
def choose_school():
    """
    学生选择学校
    """
    while True:
        # 1 获取学校信息列表
        school_list = common_interface.get_school_list()
        if not school_list:
            print("学校不存在")

        # 2 打印课程信息
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
            print("用户不存在")
            continue

        # 3 选择学校
        school_name = school_list[choise]
        flag, msg = student_interface.choose_school_interface(student_info.get('user'), school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.lagoin_auth('student')
def choose_course():
    """
    选择课程
    """
    while True:
        # 通过学生类中去查找学生所在学校列表
        flag, school_course_list = student_interface.get_school_course_list(student_info.get('user'))
        if not flag:
            print(school_course_list)

        # 2 打印学生所在的课程
        for inex, course in enumerate(school_course_list):
            print(inex, course)

        # 3 选择学校
        choise = input("请输入课程编号")
        if choise == 'q':
            break

        if not choise.isdigit():
            print("输入课程不存在")
            continue

        choise = int(choise)

        if choise not in range(len(school_course_list)):
            print("用户不存在")
            continue

        course_name = school_course_list[choise]

        # 3调用选择课程接口
        flag, msg = student_interface.choose_course_interface(student_info.get('user'), course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.lagoin_auth('student')
def check_score():
    """
    查看学生信息
    """
    flag, msg = student_interface.check_score_interface(student_info.get('user'))
    if flag:
        print(f"学生成绩{msg}")
    else:
        print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
}


def student_view():
    while True:
        print('''
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看成绩
        q.退出
        ''')

        choice = input("请输入功能视图")
        if choice == 'q':
            break

        if choice not in func_dic:
            print("输入错误")
            continue

        func_dic.get(choice)()
