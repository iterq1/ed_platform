# Generated by Django 2.2.6 on 2022-06-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=models.TextField(default='text'),
        ),
    ]
