from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import (Teacher,Subject, User)


class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    city = forms.CharField(max_length=32, help_text='City name')
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name','last_name','email','city', 'subject')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.interests.add(*self.cleaned_data.get('subject'))
        return user


class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    city = forms.CharField(max_length=32, help_text='City name')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name','last_name','email','city')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        return user

