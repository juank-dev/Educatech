from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),
    path('students/', students.homepage, name='students'),
    path('teachers/', teachers.homepage, name='teachers'),
    ]
