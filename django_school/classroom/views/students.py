from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from ..decorators import student_required
from ..forms import StudentSignUpForm
from ..models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        print(kwargs)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students')

@login_required
@student_required
def homepage(request):
    return render(request, 'classroom/students/home.html')

@login_required
@student_required
def search(request):
    if request.GET["search_teacher"]:
        msg="Teacher Found subject: {}".format(request.GET["search_teacher"])
    else:
        return render(request, 'classroom/students/home.html')
    return render(request, 'classroom/students/search.html', {'msg':msg})

class ProductListView(ListView):
    template_name = 'app2.html'
    queryset = Subject.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'List of Subjects'
 

        return context

class ProductDetailView(DetailView):
    model = Subject
    template_name = 'subjects.html'

class ProductSearchListView(ListView):
    
    template_name = 'classroom/search.html'

    def get_queryset(self):
        return Subject.objects.filter(name__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['subject_list'].count()

        return context