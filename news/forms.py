from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:                         #file:///C:\Pythontest3\README.md#news-forms-py
        model = News
        fields = ['title', 'content', "cr_avtor", 'is_published']
        
""" Форма для создания и редактирования постов.
    Подробнее о полях формы можно прочитать в разделе 
"Ключевые файлы": file:///C:\Pythontest3\README.md#L55
"""        