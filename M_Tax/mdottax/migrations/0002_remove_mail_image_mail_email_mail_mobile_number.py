# Generated by Django 5.0.6 on 2024-06-25 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdottax', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='image',
        ),
        migrations.AddField(
            model_name='mail',
            name='email',
            field=models.EmailField(default='abxc@gmail.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='mail',
            name='mobile_number',
            field=models.CharField(default='03480976172', help_text='Enter your mobile number', max_length=20, unique=True),
        ),
    ]