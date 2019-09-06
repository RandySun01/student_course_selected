import os
import pickle
from conf import settings

"""
@author RansySun
@create 2019-08-31-15:32
"""

#############################################
#
#      读/取数据库
#############################################

def db_save(obj):
    """
    保存对象信息
    :param obj: 对象
    """
    # 1 获取类名
    class_name = obj.__class__.__name__
    file_path = os.path.join(settings.DB_PATH, class_name)

    # 2 判断文件是否存在
    if not os.path.isdir(file_path):
        os.mkdir(file_path)

    # 3 保存数据信息
    user_path = os.path.join(file_path, obj.name)
    with open(user_path, 'wb') as fw:
        pickle.dump(obj, fw)


def db_select(cls, username):
    """
    取对象
    :param cls: 类名
    :param username: 对象名称
    :return: 返回类对象，默认为NOne
    """
    # 1 获取类名凭借路径
    class_name = cls.__name__

    file_path = os.path.join(settings.DB_PATH, class_name)

    # 2 判断文件夹是否存在
    if os.path.isdir(file_path):
        user_path = os.path.join(file_path, username)
        # 判断文件是否存在，读取数据
        if os.path.exists(user_path):
            with open(user_path, 'rb') as fr:
                data = pickle.load(fr)
                return data
