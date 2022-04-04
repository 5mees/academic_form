from django import forms
from .models import Academic


class AcademicForm(forms.ModelForm):
    class Meta:
        model = Academic
        fields = '__all__'


