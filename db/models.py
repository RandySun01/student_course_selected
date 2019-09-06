from db import db_handler

"""
@author RansySun
@create 2019-08-31-15:31
"""


class Base:

    def save(self):
        """
        保存对象
        """
        db_handler.db_save(self)

    @classmethod
    def select(cls, username):
        """
        读取对象信息
        :param username: 对象名称
        :return: 返回对象
        """
        return db_handler.db_select(cls, username)


class Admin(Base):
    def __init__(self, username, pwd):
        """
        初始化管理员信息
        :param username: 用户名
        :param pwd: 密码
        """
        self.name = username
        self.pwd = pwd
        self.save()

    def create_school(self, school_name, school_addr):
        """
        通过管理员创建学校
        :param school_name:
        :param school_addr:
        """
        # 创建学校
        School(school_name, school_addr)

    def create_teacher(self, teacher_name, teacher_pwd):
        """
        通过管理员创建老师
        :param teacher_name:
        :param teacher_pwd:
        """
        # 创建老师
        Teacher(teacher_name, teacher_pwd)

    def create_course(self, school_name, course_name):
        """
        通过管理员为学校创建课程
        :param school_name:
        :param course_name:
        """
        # 1 为学校创建课程

        school_obj = School.select(school_name)
        Course(course_name)

        # 2 将课程绑定给学校
        school_obj.add_school_course(course_name)


class School(Base):
    def __init__(self, school_name, school_addr):
        """
        初始化学校信息
        :param school_name:
        :param school_addr:
        """
        self.name = school_name
        self.addr = school_addr
        self.school_course_list = []
        self.save()

    def add_school_course(self, course_name):
        """
        添加课程
        :param course_name:
        """
        self.school_course_list.append(course_name)
        self.save()


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        """
        初始化信息
        :param teacher_name:
        :param teacher_pwd:
        """
        self.name = teacher_name
        self.pwd = teacher_pwd
        self.teacher_course_list = []
        self.save()

    def add_teacher_course(self, course_name):
        """
        为老师添加课程
        :param course_name:
        """
        self.teacher_course_list.append(course_name)
        self.save()

    def check_course(self):
        """
        查看老师课程
        :return:
        """
        return self.teacher_course_list

    def choose_course(self, course_name):
        """
        为老师添加课程
        :param course_name:
        """
        self.teacher_course_list.append(course_name)
        self.save()

    def check_student(self, course_name):
        """
        查看学生
        :param course_name:
        :return:
        """
        course_obj = Course.select(course_name)
        student_list = course_obj.course_student_list
        return student_list

    def change_score(self, course_name, student_name, score):
        """
        修改学生成绩
        :param course_name:
        :param student_name:
        :param score:
        """
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()


class Course(Base):
    def __init__(self, course_name):
        """
        初始化课程
        :param course_name:
        """
        self.name = course_name
        self.course_student_list = []
        self.save()

    def add_course_student(self, student_name):
        """
        将学生选择的课程进行绑定
        :param student_name:
        """
        self.course_student_list.append(student_name)
        self.save()
        print(f"课程中的学生{self.course_student_list}")


class Student(Base):
    def __init__(self, student_name, student_pwd):
        """
        学生初始化
        :param student_name:
        :param student_pwd:
        """
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.student_course_list = []
        self.score = {}
        self.save()

    def choose_school(self, school_name):
        """
        选择学校
        :param school_name:
        """
        # 选择学校
        self.school = school_name
        self.save()

    def choose_course(self, course_name):
        """
        选择课程，初始化学生成绩，并将学生学的课程添加到课程中
        :param course_name:
        """
        # 添加课程可成绩
        self.student_course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

        # 将学生绑定到选择的课程上面
        course_ojb = Course.select(course_name)
        course_ojb.add_course_student(self.name)

    def check_score(self):
        """
        查看成绩
        :return:
        """
        return self.score
