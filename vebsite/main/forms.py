from .models import Task
from django.forms import ModelForm, widgets, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","task"]
        widgets = {"title":TextInput(attrs={'class':'form-control', 'placeholder':'Введине название'}),
            "task": Textarea(attrs={'class': 'form-control', 'placeholder': 'Введине описание'}),
        }