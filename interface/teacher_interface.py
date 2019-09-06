from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def login_interface(username, pwd):
    """
    老师登录接口
    :param username:
    :param pwd:
    :return:
    """
    teacher_obj = models.Teacher.select(username)
    # 1 判断用户是否存在
    if not teacher_obj:
        return False, f'{username}用户不存在'

    # 2 判断密码是否相同
    if teacher_obj.pwd == pwd:
        return True, F"{username}登录成功"
    else:
        return False, "用户名或密码错误"


def check_course_interface(teacher_name):
    """
    查看老师教授的课程
    :param teacher_name:
    :return:
    """
    # 1获取老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 2 通过老师类，获取课程列表
    teacher_course_list = teacher_obj.check_course()
    return True, teacher_course_list


def choose_course_interface(teacher_name, course_name):
    """
    老师选择课程接口
    :param teacher_name:
    :param course_name:
    :return:
    """
    teacher_obj = models.Teacher.select(teacher_name)
    # 1 查看课程是否选择
    flag, teacher_course_list = check_course_interface(teacher_name)
    if course_name in teacher_course_list:
        return False, f'{course_name}课程已存在'

    # 2 保存老师选择的课程
    teacher_obj.choose_course(course_name)
    return True, f"{teacher_name}选择{course_name}课程选择成功"


def check_student_interface(teacher_name, course_name):
    """
    选择课程
    :param teacher_name:
    :param course_name:
    :return:
    """
    # 1 获取老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 2 让老师去产看课程下的学生
    student_list = teacher_obj.check_student(course_name)

    if student_list:
        return True, student_list
    else:
        return False, "课程下没有学生"


def change_score_interface(teacher_name, course_name, student_name, score):
    """
    通过老师修改成绩
    :param teacher_name:
    :param course_name:
    :param student_name:
    :param score:
    :return:
    """
    teacher_obj = models.Teacher.select(teacher_name)

    # 让老师去修改课程成绩
    teacher_obj.change_score(course_name, student_name, score)
    return True, '修改成功'

