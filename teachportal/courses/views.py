from django.shortcuts import render


# Create your views here.
from courses.models import Teacher, Student, Course, Group, Schedule


def index(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    courses = Course.objects.all()
    groups = Group.objects.all()
    schedules = Schedule.objects.all()
    context = {
        'teachers': teachers,
        'students': students,
        'courses': courses,
        'groups': groups,
        'schedules': schedules

    }
    return render(
        request,
        'courses/index.html',
        context=context
    )
