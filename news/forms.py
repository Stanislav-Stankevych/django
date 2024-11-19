# blog/forms.py
from django import forms
from .models import News
from django import forms
from .models import News

class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Введите заголовок',
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Введите содержание',
                'rows': 4,
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'rounded',
            }),
        }

# [Форма регистрации](file:///C:\Pythontest3\blog\forms.py#L10)


class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control border-gray-300 rounded-md px-4 py-2 w-full',
            'placeholder': 'Введите запрос для поиска...',
        })
    )