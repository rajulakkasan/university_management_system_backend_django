# Generated by Django 4.2.11 on 2024-04-24 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readdb', '0007_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('professor', 'Professor'), ('student', 'Student')], default='student', max_length=32),
        ),
    ]