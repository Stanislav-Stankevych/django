# Generated by Django 4.1 on 2024-11-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_news"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Article",
        ),
        migrations.AddField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]