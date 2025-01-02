# Generated by Django 5.0.6 on 2024-07-07 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('email', models.EmailField(default='abxc@gmail.com', max_length=254, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('mobile', models.CharField(default='', help_text='Enter your mobile number', max_length=16, unique=True)),
                ('message', models.TextField(default='this is simple message')),
            ],
            options={
                'verbose_name_plural': 'E-mails',
            },
        ),
    ]