# Generated by Django 4.2.6 on 2024-06-18 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_problem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createbooking',
            name='image',
        ),
        migrations.RemoveField(
            model_name='createbooking',
            name='item_count',
        ),
    ]