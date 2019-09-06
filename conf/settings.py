import os

"""
@author RansySun
@create 2019-08-31-14:36
"""

##################################
#       数据保存路径             #
##################################
BASE_PATYH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(
    os.path.dirname(BASE_PATYH), 'db'
)
