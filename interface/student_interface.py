from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def register_interface(username, pwd):
    """
    学生注册接口
    :param username:
    :param pwd:
    :return:
    """
    # 1 判断用户是否存在
    student_obj = models.Student.select(username)
    if student_obj:
        return False, f'{username}用户已经存在'
    # 2 注册
    models.Student(username, pwd)
    return True, f"{username}注册成功"


def login_interface(username, pwd):
    """
    学生登录接口
    :param username:
    :param pwd:
    :return:
    """
    student_obj = models.Student.select(username)
    # 1 判断用户是否存在
    if not student_obj:
        return False, f'{username}用户不存在'

    if student_obj.pwd == pwd:
        return True, F"{username}登录成功"
    else:
        return False, "用户名或密码错误"


def choose_school_interface(student_name, school_name):
    """
    选择学校接口
    :param student_name:
    :param school_name:
    :return:
    """

    # 1 判断学生是否选择了学校
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False, f"{student_name}学生已经选择的学校"

    # 2 通过学生类选择学校
    student_obj.choose_school(school_name)
    return True, f"{student_name}选择了{school_name}学校成功"


def get_school_course_list(student_name):
    """
    获取学生所在的学校
    :param student_name:
    :return:
    """
    # 1获取学生所在学校的课程
    student_obj = models.Student.select(student_name)
    if not student_obj.school:
        return False, f"没有选择学校请去选择学校"
    # 2 获取学校名称
    school_name = student_obj.school
    # 3获取学生对象
    school_obj = models.School.select(school_name)
    # 4 从学校类中返回课程
    school_course_list = school_obj.school_course_list
    return True, school_course_list


def choose_course_interface(student_name, course_name):
    """
    选择课程的接口
    :param student_name:
    :param course_name:
    :return:
    """
    # 1 判断学生是否已经选过了这个课程
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.student_course_list:
        return False, f"{student_name}已经学过这么课程"

    # 2 学生选择课程，并将学生绑定到课程中
    student_obj.choose_course(course_name)
    return True, f"{student_name}选择了{course_name}课程"


def check_score_interface(student_name):
    student_obj = models.Student.select(student_name)
    score_dic = student_obj.check_score()
    return True, score_dic
