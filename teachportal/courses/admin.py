from django.contrib import admin

# Register your models here.
from courses.models import Teacher, Group, Student, Schedule, Course

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Course)

