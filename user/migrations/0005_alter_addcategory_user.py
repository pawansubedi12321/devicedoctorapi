# Generated by Django 4.2.6 on 2024-02-17 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_addcategory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcategory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.register'),
        ),
    ]
