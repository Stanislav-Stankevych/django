# Pythontest3 Project Documentation

<!-- TOC -->

Этот файл содержит документацию по проекту **Pythontest3**. Здесь описаны основные файлы, их назначение, а также ссылки на важные участки кода.

## Оглавление

- [Pythontest3 Project Documentation](#pythontest3-project-documentation)
  - [Оглавление](#оглавление)
  - [Установка и запуск проекта](#установка-и-запуск-проекта)
    - [Требования](#требования)
    - [Шаги для установки](#шаги-для-установки)
  - [Структура проекта](#структура-проекта)
  - [Ключевые файлы](#ключевые-файлы)
    - [models](#models)
    - [urls](#urls)
    - [views (представление)](#views-представление)
    - [forms](#forms)
  - [Команды-для-терминала](#команды-для-терминала)
    - [Команды для Django](#команды-для-django)
    - [Команды для GitHub](#команды-для-github)
    - [Команды для conda](#команды-для-conda)
  - [Функции и их реализация](#функции-и-их-реализация)
    - [Функции](#функции)
      - [render();](#render)
      - [path();](#path)

---

[Шаги для установки](#Шаги-для-установки)

## Установка и запуск проекта

### Требования

- Python 3.9+
- Django 4.1
- PostgreSQL

### Шаги для установки

1. Установите зависимости:
   ```bash
   conda env update -f environment.yml
   ```

## Структура проекта

Проект организован следующим образом:

Pythontest3/
├── blog/
│ ├── migrations/
│ ├── templates/
│ ├── forms.py # Форма для добавления постов
│ ├── models.py # Модели базы данных
│ └── views.py # Представления для блога
├── main/
│ ├── templates/
│ ├── forms.py # Форма для регистрации пользователей
│ └── views.py # Основные представления
└── README.md # Основной файл документации

## Ключевые файлы

### models

[blog/models.py](blog/models.py)

Файл содержит модели базы данных для блога. Модель общается с базой даных, за счет этого
можно проделывать все дейсивия - обновлять, дополнять, изменять данные в таблицы.
Модель описывается classom который принимает из главных аргументов models.Model который
экспортируем из библиотеки django.db
Пример использования кода:

from django.db import models

```python
class Post(models.Model):
    title = models.CharField(max_length=200)              # Заголовок поста
    content = models.TextField()                          # Содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания поста
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления поста
    is_published = models.BooleanField(default=True)      # Поле для публикации поста


    def __str__(self):
        return self.title
```

### urls

[blog/urls.py](blog/urls.py)

Этот файл содержит в себе шаблоны (шаблоны URL-адресов - urlpatterns)
Здесь функция path импортируется из библиотеки django.urls и принимает в себя параметры:

```python

from django.urls import path
from . import views

urlpatterns = [
path("", views.post_list, name='post_list'),
path('', views.article_list, name='article_list'),
path('create/', views.create_post, name='create_post'), # добавляем новый маршрут
path('<int:post_id>/', views.post_detail, name='post_detail'), # Детальная страница поста
]

```

1. **""** - Так как первый параметр пустой функция сработает если адрес был:**http://127.0.0.1:8000/blog**
   так как после папки блог других адресов нету. Но почему имено blog а не news или любой другой параметр.
   Все дело в том что в папке основного пронкта **myproject** тоже есть файл urls.py в котром прописываются
   направление к приложение и вот как это выглядит:

```python

from django.contrib import admin
from django.urls import path, include
from main import views as main_views  # Импортируем представления из приложения main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),# Все URL с префиксом blog/ идут в приложение blog и дальше распределяет который находится в блоге
    path('news/', include('news.urls')),  # Все URL с префиксом news/ идут в приложение news
    path('', main_views.home, name='home'),  # Указываем main_views.home # Главная страница проекта
#main/views - home
]

```

Как мы здесь видим в коде написано если url заканчивается на blog то мы должны использовать приложенин blog и файл urls
**http://127.0.0.1:8000/blog** и blog/urls в котором мы определяем какую функцию выполнять см.п.1 начало

2. Указывает, что URL create/ показывает что как только в браузере появиться страница
   по адрессу http://127.0.0.1:8000/blog/create то сразу срабатывает функция **create_post()**
   которая находится в файле views. Так как этот файл urls.py находится в приложении blog
   то методы patch срабатывают только после сылки http://127.0.0.1:8000/blog тоесть вот в
   такой сылки сработают две функции **post_list()** и **article_list()** в файле blog/views.py
   так как первый аргумент в методе path пустой.
   _int:post_id_
   Здесь _int:id_ — это параметр, который Django передаст в функцию article*detail в качестве аргумента id.
   URL /blog/articles/5/ направит пользователя на представление post_detail с параметром id=5.
   \_int:...* указывает тип параметра (целое число). Вы также можете использовать _str:..._ для строковых параметров.

```python

path('<int:post_id>/', views.post_detail, name='post_detail')

```

Надо пояснить что сработает только в том случаи если URL будет с любым номером: http://127.0.0.1:8000/blog/5

3. Функция которая должна сработать в файле **blog/views.py** и выполниить действия
   В Django каждый маршрут должен быть уникальным, иначе сработает только первый из них.
   Поэтому либо используйте уникальные пути, либо структурируйте URL-ы с помощью namespace для
   разных приложений вот пример:

```python
urlpatterns = [
    path("blog/", include("blog.urls", namespace="blog")),
    path("articles/", include("articles.urls", namespace="articles")),
]
```

1. В параметре **name** в третьем аргументе функции path в Django указывается уникальное имя
   для каждого URL-шаблона. Это имя используется для:

- Обратного построения URL-адресов: позволяет ссылаться на URL в шаблонах и в коде Python
  без необходимости жёстко прописывать URL-адрес. Если в будущем путь изменится, все ссылки
  автоматически обновятся при изменении имени.
- Упрощения работы с URL в шаблонах и представлениях: можно вызывать URL, используя **reverse()**
  в представлениях и **{% url %}** в шаблонах.
  Пример использования:
  В шаблоне:

```python

<a href="{% url 'news_detail' news_id=news.id %}">Подробнее</a>
```

В представлении:

```python

from django.urls import reverse
return redirect(reverse('news_detail', args=[news_id]))
```

Каждое имя (news_list, create_news, news_detail) уникально и позволяет Django
точно идентифицировать нужный URL.

### views (представление)

1. Этот файл содержит в себе множество функций которые реализовывает для приложения
   в каждом приложении есть свой файл с реализацией своих функций. Вот пример приложения
   blog/views:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def article_list(request):
    articles = Post.objects.all()
    return render(request, 'blog/article_list.html', {'articlesscilk': articles})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

```

Каждая из этих функций наследует класс Post а потом получает все обьекты класса
а потом использует встроенную функцию **render()** назначение которой передовать
полученные данные (рендерить) в указаанную html страницу в нашем примере post_list.html,
По сути

[Перейти к строке 10 в forms.py](blog/forms.py#L10)

Перейти к файлу

[blog/forms.py]

Содержит форму для добавления новых публикаций. Она определяет виджеты и стили для полей формы.

Перейти к файлу

[main/forms.py]

Файл с формой для регистрации новых пользователей. Включает поля для имени пользователя, пароля и email.

### forms

[news/forms.py](news/forms.py)

```python
from django import forms

```

1. Импортируя библиотеку в Django - forms мы можем обратиться к адному из его class а именно **forms.ModelForm**
   который позволяет создавать формы как пример форма для создания новости:

```python
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published']
```

При создании **class NewsForm** мы передаем в него в качестве аргумента **class ModelForm**
так мы наследуем все его свойства и методы котрый Django подготовил для нас что облегчает нам
создание своей формы.
Второй **class Meta:** который внутрии класса **class NewsForm** необходим для обращении к таблицы
база данных через созданную нами класс News в файле _models.py_ и манипуляции с ним. Из всего изложеного
можно понять что этот файл служи для настройки формы с таблицей базы данных.

2. Форма на основе модели NewsForm
   Для создания формы, связанной с этой моделью, используется ModelForm, что позволяет Django автоматически
   создать HTML-форму с полями, соответствующими полям модели:

```python


from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published']

```

Класс Meta:

Атрибут _model = News_ связывает форму с моделью News. Это означает, что Django автоматически создаст форму с полями,
соответствующими полям модели News.
Атрибут _fields = ['title', 'content', 'is_published']_ указывает, какие поля модели включить в форму.
В данном случае в форму будут включены только title, content, и is*published.
Поля \_created_at* и _updated_at:_

Поля created_at и updated_at не включены в форму, так как они управляются автоматически: created_at задаётся
при создании записи, а updated_at обновляется при каждом изменении записи. Их исключение из формы позволяет
избежать их ручного редактирования. 3. Как использовать эту форму в представлении
Теперь, когда форма создана, вы можете использовать её в представлении для создания и редактирования записей:

```python

# views.py
from django.shortcuts import render, redirect
from .forms import NewsForm

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные формы в базе
            return redirect('news_list')  # Перенаправляем на список новостей
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

```

В этом примере:

Если запрос POST, форма создаётся с данными из запроса (request.POST), и при успешной валидации данные сохраняются в базе.
Если запрос GET, отображается пустая форма для ввода данных. Шаблон для отображения формы.
Чтобы форма отображалась на веб-странице, нужно создать шаблон. Пример шаблона create_news.html:

```html
Копировать код
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <!-- Каждое поле формы отображается в параграфе (<p>) -->
  <button type="submit">Сохранить новость</button>
</form>
```

4. Преимущества использования ModelForm
   Связь с моделью: ModelForm автоматически привязывает форму к модели, что упрощает работу с формой и сохраняет данные напрямую в базу.
   Автоматическая валидация: ModelForm наследует валидацию от модели, например, проверяет длину строк, обязательные поля и т. д.
   Удобство: ModelForm сокращает количество кода и облегчает управление полями формы, так как не нужно вручную прописывать все атрибуты полей.
   Таким образом, представленный код является достаточно полным и готовым для работы с формой, связанной с моделью News.
5. Стилилизация формы

```python
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
```

c помощью widgets={ } мы можем добавить нужные классы в каждое поле что помогает нам сделать стилилизацию формы

## Команды-для-терминала

### Команды для Django

_Команда для создания проекта в текущей директории_

**django-admin startproject nameproject**

Объяснение:
Без точки . Django создаёт новую папку с именем проекта внутри
текущей директории, и все файлы проекта размещаются внутри неё.
С точкой . Django использует текущую директорию для создания
файлов проекта, не создавая дополнительной вложенной папки.
Где myproject — название вашего проекта.

_Команда для запуска виртуального сервера на python адресс: http://127.0.0.1:8000_

**python manage.py runserver**

_Команда для создания миграций изменений в моделях_

**python manage.py makemigrations**
_Применяет миграции базы данных_

```html
python manage.py migrate
```

_Команда для создания администратора для панели управления Django_

```console
python manage.py createsuperuser
```

И все они работают через python, потому что это команды, выполняемые в контексте проекта и
управляемые самим интерпретатором Python, а не pip.

### Команды для GitHub

1.  _Настроить Git и сделать коммит_

После всех этих изменений добавьте файлы в Git и сделайте коммит:
**git add .**
**git commit -m "Здест напиши свой коментарий к соханению"**

2.  _Сообщение Git о замене LF на CRLF_

- Указывает, что файлы, которые вы добавляете в коммит (package.json и package-lock.json), имеют разные символы окончания строки.

- Что такое LF и CRLF?
  LF (Line Feed): Это стандартный символ окончания строки для Unix/Linux и macOS.
  CRLF (Carriage Return + Line Feed): Стандартный символ окончания строки для Windows.
  Почему возникает это предупреждение?
  Когда вы добавляете файлы в Git на Windows, Git по умолчанию может преобразовывать окончания строк из LF в CRLF и обратно для совместимости с разными операционными системами. Это поведение может вызвать такие предупреждения, если окончания строк не совпадают с ожидаемыми на вашей системе.

  - Как убрать предупреждение?
    Настройка Git для автоматического преобразования: Вы можете установить настройку Git, чтобы он автоматически обрабатывал окончания строк в зависимости от операционной системы. В командной строке выполните:
    **git config --global core.autocrlf true**
    true — Git автоматически конвертирует LF в CRLF при клонировании репозитория на Windows и обратно при коммите. Это рекомендуется для работы на Windows.
    false — Полностью отключает конвертацию. Это рекомендуется, если вы работаете только в средах Linux или macOS.

3.  _Откат всех изменений с момента последнего коммита_

- Если ты хочешь просто отменить все несохраненные изменения (например, изменения в файлах, которые ты не коммитил), то можно использовать команду:

**git checkout .**
Эта команда откатит все изменения в файлах до состояния последнего коммита.

_Откат к последнему коммиту, включая удаление новых файлов_

- Если ты добавил новые файлы, которые не были закоммичены, и хочешь удалить их, используй:

**git clean -fd**
Эта команда удалит все неотслеживаемые файлы и папки. Будь осторожен, так как она необратима для новых файлов, которые не добавлены в коммит.

_Полный откат изменений и сброс HEAD к последнему коммиту_

- Если ты добавил изменения в staged (использовал git add) или просто хочешь полностью вернуть проект к состоянию последнего коммита, можно использовать команду reset:

**git reset --hard HEAD**

- Эта команда: Сбрасывает все изменения, которые были сделаны после последнего коммита.
  Откатывает все файлы, в том числе staged.
  Внимание: --hard удаляет все изменения без возможности восстановления, так что используй эту команду с осторожностью.

### Команды для conda

_Создай новую среду с нужной версией Python:_

**conda create -n my_django_env python=3.13**

Замените my_django_env на любое имя для твоей среды.
Conda скачает Python и создаст изолированное окружение.

_Активируй среду:_

**conda activate my_django_env**

_Установи Django и psycopg2 в этой среде:_

conda install django psycopg2
_Команда показывает все среды для работы_

**conda info --envs**

_Проверь, что осталась одна версия Conda_

**conda -V**
**conda --version**

_Удалите окружение: Выполните следующую команду, чтобы удалить окружение virtual:_

**conda remove -n virtual --all**

Виртуальное окружение в Python — это изолированная среда, которая содержит собственную копию
интерпретатора Python и всех необходимых библиотек. Оно позволяет устанавливать и использовать
зависимости (пакеты и библиотеки) для конкретного проекта, не затрагивая другие проекты на компьютере.

Зачем нужно виртуальное окружение?
Изоляция зависимостей. Каждый проект может иметь свои собственные версии библиотек,
не влияя на другие проекты. Это особенно важно, когда разные проекты требуют разные
версии одной и той же библиотеки.

Легкость в управлении проектами. Можно легко переключаться между проектами с разными
зависимостями и не беспокоиться о конфликтах версий.

Упрощение развертывания. Используя виртуальное окружение, можно легко воспроизвести
среду разработки на других машинах (например, на сервере), обеспечивая одинаковое
поведение приложения.

Поддержка требований проекта. Виртуальное окружение позволяет сохранять зависимости
в виде файла **environment.yml**, чтобы другие разработчики могли установить такие же зависимости,
выполнив команду:

## Функции и их реализация

### Функции

#### render();

1. _render()_ - упрощает процесс передачи данных в шаблон и их отображения в браузере.
   Она является одним из наиболее часто используемых методов в Django, поскольку позволяет
   удобно обрабатывать и отображать информацию на веб-странице.

```python
render(request, template_name, context=None, content_type=None, status=None, using=None)
```

Вот основные параметры функции:

**request:** обязательный параметр, представляющий объект запроса. Он содержит всю информацию о текущем запросе от пользователя
(например, метод запроса, данные формы, заголовки и т. д.).
**template_name:** обязательный параметр, указывающий путь к HTML-шаблону, который нужно использовать для отображения страницы.
Путь обычно задается относительно папки templates (например, 'blog/post_list.html').
**context:** необязательный словарь, содержащий данные, которые вы хотите передать в шаблон. Например, {'posts': posts}.
Эти данные можно использовать в шаблоне для отображения информации.
**content_type:** тип содержимого (например, text/html). Обычно оставляется по умолчанию.
**status:** код статуса HTTP-ответа (например, 200 для успешного ответа или 404 для "не найдено").
По умолчанию используется 200.
**using:** название движка шаблонов, если в проекте используется несколько движков

2. Пример использования функции render()
   Рассмотрим, как функция render() используется в представлении для отображения списка постов:

```python

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Получаем все посты из базы данных
    context = {'posts': posts}  # Создаем словарь данных для передачи в шаблон
    return render(request, 'blog/post_list.html', context)  # Отправляем данные в шаблон

```

В этом примере:
**request** — объект запроса, переданный функции представления.
**blog/post_list.html** — шаблон HTML, который будет использоваться для отображения.
**context** — словарь данных, который содержит переменные (здесь это posts), передаваемые в шаблон.

В шаблоне post_list.html можно использовать переданные данные. Например:

```html
<!doctype html>
<html>
  <head>
    <title>Список постов</title>
  </head>
  <body>
    <h1>Список постов</h1>
    <ul>
      {% for post in posts %}
      <li>{{ post.title }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

Реализация функции render() за кулисами
За кулисами render() в основном выполняет следующие шаги:

Загрузка шаблона: Django ищет и загружает шаблон, указанный в template*name.
Обработка контекста: Все данные из context передаются в шаблон.
Рендеринг: Django обрабатывает шаблон, заполняя его данными из context (заменяет переменные в шаблоне на значения).
Создание HttpResponse: Рендеринг возвращает строку HTML, которая используется для создания объекта HttpResponse.
Возвращение ответа: \*\_render()* возвращает объект HttpResponse с готовым HTML-содержимым.

Заключение
render() — это основная функция для работы с шаблонами в Django, которая облегчает отображение данных и создание
ответа на основе шаблона. Она делает код более понятным и чистым, а также помогает легко интегрировать данные из
базы в HTML-код для отображения на сайте.

#### path();

Функция path() в Django используется для определения маршрутов (URL-адресов), связывая URL с конкретным представлением (view).
Она является частью модуля django.urls и используется для маршрутизации запросов в urls.py.

Функция _path()_ определяет путь, по которому Django направит запрос пользователя к соответствующему представлению.

```python

path(route, view, kwargs=None, name=None)

```

Параметры функции _path()_
**route** (обязательный) — строка, представляющая URL-шаблон, который будет сопоставлен с запросом.

Путь указывается относительно корневого URL проекта.
Можно использовать динамические сегменты, например, '<int:id>/'.
view (обязательный) — ссылка на функцию или класс представления, которое будет вызываться, если URL
соответствует указанному пути.

Это может быть как функция, так и класс.
Например, **views.home** или **MyView.as_view()**.
**kwargs (необязательный)** — дополнительные аргументы, передаваемые в представление в виде словаря.

Эти аргументы могут быть использованы для настройки представления.
Например, kwargs={'slug': 'example'}.
**name (необязательный)** — строка, представляющая имя маршрута.
Используется для создания ссылок на URL в шаблонах через тег {% url %}.
Это особенно полезно, если путь может измениться, так как имя маршрута
остаётся неизменным и помогает избежать изменения всех ссылок в шаблонах.

Пример использования path()
Пример файла urls.py:

```python

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Динамический URL для деталей поста
]

path('', views.home, name='home') связывает URL корневого пути '' (главная страница) с представлением views.home.
path('about/', views.about, name='about') связывает URL /about/ с представлением views.about.
path('post/<int:id>/', views.post_detail, name='post_detail') — динамический маршрут, где <int:id>
 принимает целое число и передает его в представление как параметр id. Например, URL /post/5/ вызовет views.post_detail с параметром id=5.
```

```js
1. Динамические сегменты в route
int:id — задает параметр id типа int (целое число), который передается в представление.
Django поддерживает типы: str, int, slug, uuid и path.
str: строка без символов /
int: целое число
slug: строка, содержащая буквы, цифры, дефисы и подчеркивания (удобно для SEO-friendly URL)
uuid: универсальный уникальный идентификатор (UUID)
path: любая строка, включая символы
```

2. Использование имен маршрутов в шаблонах
   Если вы дали маршруту имя, его можно использовать в шаблоне для создания ссылок:

html
<a href="{% url 'post_detail' id=5 %}">Подробнее о посте</a>
Это создаст ссылку на URL с именем post_detail и параметром id=5, которая указывает на путь /post/5/.

Заключение
Функция path() — это основной способ определения маршрутов в Django. Она позволяет связывать URL с
представлениями, указывать динамические параметры, передавать дополнительные аргументы и задавать имена
маршрутов для удобного создания ссылок в шаблонах.
