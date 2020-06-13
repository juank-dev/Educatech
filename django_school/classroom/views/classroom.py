from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages

from django.contrib.auth import authenticate

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            messages.success(request, 'Welcome Teacher {} {}'.format(request.user.first_name, request.user.last_name))
            return redirect('teachers:teachers')
        else:
            messages.success(request, 'Welcome Student {} {}'.format(request.user.first_name, request.user.last_name))
            return redirect('students:students')
    return render(request, 'classroom/home.html')
