# Generated by Django 4.2.6 on 2024-03-02 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_createbooking_problem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createbooking',
            name='booked_problem',
        ),
    ]
