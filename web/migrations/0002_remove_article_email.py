# Generated by Django 4.0.3 on 2022-03-10 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='email',
        ),
    ]