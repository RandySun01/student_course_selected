from db import models

"""
@author RansySun
@create 2019-08-31-15:32
"""


def register_interface(username, pwd):
    """
    管理员注册接口
    :param username:
    :param pwd:
    :return:
    """
    # 1 判断用户是否存在
    admin_obj = models.Admin.select(username)
    if admin_obj:
        return False, f'{username}用户已经存在'
    # 2 注册
    models.Admin(username, pwd)
    return True, f"{username}注册成功"


def login_interface(username, pwd):
    """
    管理员登录接口
    :param username:
    :param pwd:
    :return:
    """
    admin_obj = models.Admin.select(username)
    # 1 判断用户是否存在
    if not admin_obj:
        return False, f'{username}用户不存在'

    # 2 判断密码是否正确
    if admin_obj.pwd == pwd:
        return True, F"{username}登录成功"
    else:
        return False, "用户名或密码错误"


def create_school_interface(admin_user, school_name, school_addr):
    """
    通过管理员创建学校
    :param admin_user:
    :param school_name:
    :param school_addr:
    :return:
    """
    # 1判断学校是否存在
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, f"{school_name}学校已经存在"

    # 2 通过管理员创建
    admin_obj = models.Admin.select(admin_user)
    admin_obj.create_school(school_name, school_addr)

    return True, f"{school_name}学校创建成功"


def create_teacher_interface(admin_name, teacher_name, teacher_pwd='123'):
    """
    通过管理员创建老师
    :param admin_name:
    :param teacher_name:
    :param teacher_pwd:
    :return:
    """
    teacher_obj = models.Teacher.select(teacher_name)
    # 1 判断老师是否存在
    if teacher_obj:
        return False, '老师已经存在'

    # 2 创建老师
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, F"{teacher_name}老师创建成功"

    pass


def create_course_interface(admin_name, school_name, course_name):
    """
    为学校创建课程
    :param admin_name:
    :param school_name:
    :param course_name:
    :return:
    """
    # 1 判断学校是否已经课程
    school_obj = models.School.select(school_name)
    if course_name in school_obj.school_course_list:
        return False, f"{school_name}学校已经含有{course_name}课程"

    admin_obj = models.Admin.select(admin_name)

    # 2 创建课程，将课程创建绑定给学校和创建课程类
    admin_obj.create_course(school_name, course_name)
    return True, "创建课程成功"


