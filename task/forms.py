from django import forms
from .models import TaskDetail

class TaskForm(forms.ModelForm):

    class Meta():
        model = TaskDetail
        fields = ('task_author', 'task_title','assign_to', 'complete_date')
