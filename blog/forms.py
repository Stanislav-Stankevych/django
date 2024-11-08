# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', "is_published" ]
#Добавление классов к полям в Meta с помощью widgets
#Это один из самых популярных методов. В классе Meta формы можно использовать атрибут widgets, чтобы настроить каждый элемент
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-title', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control-text', 'placeholder': 'Введите текст'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
