# Generated by Django 3.1.12 on 2021-06-30 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classrooms',
            name='email',
        ),
    ]