from lib import common
from interface import teacher_interface, common_interface

"""
@author RansySun
@create 2019-08-31-15:31
"""
teacher_info = {'user': None}


def login():
    """
    登录
    """
    username, pwd = common.input_username_pwd()
    flag, msg = teacher_interface.login_interface(username, pwd)
    if flag:
        print(msg)
        teacher_info['user'] = username
    else:
        print(msg)


@common.lagoin_auth("teacher")
def check_course():
    """
    查看老师选择的课程
    """
    flag, msg = teacher_interface.check_course_interface(teacher_info.get('user'))
    if flag:
        print(msg)
    else:
        print(msg)


@common.lagoin_auth("teacher")
def choose_course():
    """
    选择学生课程
    """
    while True:

        # 1 打印所有课程
        course_list = common_interface.get_course_list()
        if not course_list:
            print("没有课程")

        for indx, course in enumerate(course_list):
            print(indx, course)

        # 2 选择课程
        choise = input("请输入课程编号")
        if choise == 'q':
            break
        if not choise.isdigit():
            print("必须是数字")
            continue

        choise = int(choise)

        if choise not in range(len(course_list)):
            print("你输入的课程不存在")
            continue

        course_name = course_list[choise]

        # 3 调用选择接口
        flag, msg = teacher_interface.choose_course_interface(teacher_info.get('user'), course_name)
        if flag:
            print(msg)
        else:
            print(msg)


@common.lagoin_auth("teacher")
def check_student():
    """
    查看老师教授的课程下的学生
    """
    while True:

        # 1获取老师选择的课程
        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not course_list:
            print("课程为空，请去选择课程")

        # 2 打印课程信息
        for indx, course in enumerate(course_list):
            print(indx, course)

        # 3选择课程
        choice = input("请输入编号")
        if choice == 'q':
            break

        if not choice.isdigit():
            print("输入必须是数字")
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print("课程不存在")
            continue

        course_name = course_list[choice]

        # 4 选择课程
        flag, msg = teacher_interface.check_student_interface(teacher_info.get('user'), course_name)
        if flag:
            print(msg)
        else:
            print(msg)


@common.lagoin_auth("teacher")
def change_score():
    """
    修改课程成绩
    """
    while True:
        # 1 获取老师下面的课程

        flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
        if not course_list:
            print("课程为空，请去选择课程")

        for indx, course in enumerate(course_list):
            print(indx, course)

        # 2选择课程
        choice = input("请输入编号")
        if choice == 'q':
            break

        if not choice.isdigit():
            print("输入必须是数字")
            continue

        choice = int(choice)

        if choice not in range(len(course_list)):
            print("课程不存在")
            continue

        course_name = course_list[choice]

        # 3获取课程下的学生
        flag, student_list = teacher_interface.check_student_interface(teacher_info.get('user'), course_name)

        if not flag:
            print("课程下没有学生")
        for indx, student in enumerate(student_list):
            print(indx, student)

        # 4选择课程
        choice2 = input("请输入编号")
        if choice2 == 'q':
            break

        if not choice2.isdigit():
            print("输入必须是数字")
            continue

        choice2 = int(choice2)

        if choice2 not in range(len(student_list)):
            print("课程不存在")
            continue

        student_name = student_list[choice]

        score = input("请输入课程成绩")


        # 5 修改成绩接口
        flag, msg = teacher_interface.change_score_interface(teacher_info.get('user'), course_name, student_name, score)
        if flag:
            print(msg)

        else:
            print(msg)










func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': change_score,
}


def teacher_view():
    while True:
        print('''
            1.登录
            2.查看教授课程
            3.选择教授课程
            4.查看课程学生
            5.修改学生成绩
            q.退出
            ''')

        choice = input("请输入功能视图")
        if choice == 'q':
            break

        if choice not in func_dic:
            print("输入错误")
            continue

        func_dic.get(choice)()
