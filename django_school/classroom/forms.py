# Django
# standard library
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

# local Django
from classroom.models import (Answer, Question, Student, StudentAnswer,
                              Subject, User, Teacher)

""" 
  Here we set the fields which are going to take as a formulary, inheriting from fields of the models file  
"""
class TeacherSignUpForm(UserCreationForm):

    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name','last_name','email','city', 'subject', 'image_profile', 'description')

    @transaction.atomic
    """ Decorator to save the subject as a teacher """
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.interests.add(*self.cleaned_data.get('subject'))
        return user

"""
    - Setting the formulary fields
    - Saving the data
"""
class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name','last_name','email','city','interests')

    @transaction.atomic
    def save(self):
        """ Decorator to save the subject as a stundent """
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user

class StudentInterestsForm(forms.ModelForm):
    """ Setting the field of the students interest"""
    class Meta:
        model = Student
        fields = ('interests', )
        widgets = {
            'interests': forms.CheckboxSelectMultiple
        }


class QuestionForm(forms.ModelForm):
    """ Creating by text the questions formulary"""
    class Meta:
        model = Question
        fields = ('text', )


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    """ Cleaning the fields previously filled"""
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


class TakeQuizForm(forms.ModelForm):
    """ Formulary previously made by the teacher, to take the quiz by the student"""
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')