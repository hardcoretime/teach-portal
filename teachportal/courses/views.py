from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'description']

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.pk})


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['name', 'description']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses')
