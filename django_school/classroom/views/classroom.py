from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        print("autenticacion ok")
        if request.user.is_teacher:
            return redirect('teachers')
        else:
            return redirect('students')
    return render(request, 'classroom/home.html')
