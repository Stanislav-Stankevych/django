# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control-title w-full p-2 border border-gray-300 rounded-md',
                'placeholder': 'Введите заголовок'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control-text w-full p-2 border border-gray-300 rounded-md',
                'placeholder': 'Введите текст'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }
# [Форма регистрации](file:///C:\Pythontest3\blog\forms.py#L10)