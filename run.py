from core import src
import os
import sys
"""
@author RansySun
@create 2019-08-31-15:31
"""
# 添加到环境变量
sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)
if __name__ == '__main__':
    src.run()