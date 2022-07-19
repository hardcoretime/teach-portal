from django.db import models


# Create your models here.
class TeachPortalUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'


class Teacher(TeachPortalUser):
    subject = models.CharField(max_length=50)


class Student(TeachPortalUser):
    bio = models.TextField(max_length=500, null=True, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson_datetime = models.DateTimeField(verbose_name='lesson datetime')
    theme = models.CharField(max_length=100)
