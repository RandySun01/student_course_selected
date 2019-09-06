from core import admin
from core import student
from core import teacher

"""
@author RansySun
@create 2019-08-31-15:33
"""
func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


def run():
    while True:
        print('''
                1.管理员视图
                2.学生视图
                3.老师视图
                q.退出
                ''')
        choice = input("请输入功能视图")
        if choice == 'q':
            break

        if choice not in func_dic:
            print("输入错误")
            continue

        func_dic.get(choice)()
