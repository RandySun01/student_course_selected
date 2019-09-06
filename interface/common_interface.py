import os
from conf import settings

"""
@author RansySun
@create 2019-08-31-15:32
"""


def get_school_list():
    """
    获取学校列表，管理员为学校创建课程和学生选择学校
    :return: 返回list
    """
    file_path = os.path.join(settings.DB_PATH, 'School')
    if os.path.exists(file_path):
        return os.listdir(file_path)


def get_course_list():
    """
    获取课程列表，用于老师选择的课程
    :return: 返回list
    """
    file_path = os.path.join(settings.DB_PATH, 'Course')
    if os.path.exists(file_path):
        return os.listdir(file_path)
