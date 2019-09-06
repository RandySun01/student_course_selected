"""
@author RansySun
@create 2019-08-31-15:33
"""


def lagoin_auth(auth):
    """
    装饰器
    :param auth: 逻辑判断
    :return:
    """

    def innter(func):

        def outter(*args, **kwargs):

            from core import admin, student, teacher

            # 1 管理员装饰器
            if auth == 'admin':
                if admin.admin_info.get('user'):

                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()

            # 2 学生装饰器
            elif auth == 'student':
                if student.student_info.get('user'):

                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()

            # 3 老师装饰器
            elif auth == 'teacher':
                if teacher.teacher_info.get('user'):

                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print("权限不足")

        return outter

    return innter


def input_username_pwd():
    """
    用户名和密码的输入
    :return:
    """
    username = input("请输入用户名")
    pwd = input("请输入密码")

    return username, pwd
