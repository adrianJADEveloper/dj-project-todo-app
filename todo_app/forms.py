from django import forms
from .models import TodoItem

# Define your forms

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'
