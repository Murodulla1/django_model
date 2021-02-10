from django.urls import path

from . import views

urlpatterns = [
    path("universitite/",views.universitite,name="name"),
    path("student-add/",views.add_student, name ="add-student"),
    path("student_list/",views.student_list,name="student-list"),
    path("add_teacher/",views.add_teacher,name="add-teacher"),
]