from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields ='__all__'


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register
		fields = '__all__'

		