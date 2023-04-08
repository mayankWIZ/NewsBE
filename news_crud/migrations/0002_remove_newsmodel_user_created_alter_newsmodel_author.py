# Generated by Django 4.2 on 2023-04-08 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsmodel',
            name='user_created',
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL),
        ),
    ]
