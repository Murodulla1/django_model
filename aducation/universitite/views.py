from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Teacher


def universitite(request):
    return HttpResponse("universitite")

def add_teacher(request):
    teacher = Teacher()
    teacher.name = "Gulzebo"
    teacher.age = 36
    teacher.nomer = 125256245
    teacher.save()
    return HttpResponse("uqituvchi qushildi")
def teacher_list(request):
    teachers = Teacher.object.all()
    for teach in teachers:
        print(teach)
    return HttpResponse("teacher_list")
def add_student(request):
    student = Student()
    student.name = "Muxammadxo`ja"
    student.group = "217-15"
    student.age = 15
    student.nomer = 1515155155
    student.save()
    return HttpResponse("Student qushildi")

def student_list(request):
    students = Student.objects.all()
    for student in students:
        print(student)
    return HttpResponse("Student List")
