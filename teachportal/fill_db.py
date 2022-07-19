import datetime
import os

import django
import pytz

os.environ["DJANGO_SETTINGS_MODULE"] = "teachportal.settings"
django.setup()

from courses.models import Student, Teacher, Course, Group, Schedule

student = Student(
    first_name='Ivan', last_name='Ivanov', email='i@ivanov.ru', bio='frontend developer'
)
student1 = Student(
    first_name='Petr', last_name='Petrov', email='p@petrov.ru', bio='backend developer'
)
student2 = Student(
    first_name='Sergey', last_name='Sergeev', email='s@sergeev.ru', bio='fullstack developer'
)

student.save()
student1.save()
student2.save()

teacher = Teacher(
    first_name='Matvey', last_name='Matveev', email='m@matveev.ru', subject='Python Django'
)
teacher.save()

course = Course(name='Web-Python', description='Django, Flask, Vue3, PostgreSQL.')
course.save()

course = Course.objects.filter(id=1).first()
group = Group(name='first', course_id=course.id)
group.save()

group = Group.objects.filter(id=1).first()
teacher = Teacher.objects.filter(id=1).first()
schedule = Schedule(
    lesson_datetime=datetime.datetime(2022, 7, 11, 20, 0, tzinfo=pytz.UTC),
    theme='OOP',
    group_id=group.id,
    teacher_id=teacher.id,
)
schedule2 = Schedule(
    lesson_datetime=datetime.datetime(2022, 7, 14, 20, 0, tzinfo=pytz.UTC),
    theme='Django Models',
    group_id=group.id,
    teacher_id=teacher.id,
)
schedule.save()
schedule2.save()
