# Generated by Django 4.0.3 on 2022-05-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_face_rec_profile_face'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='face',
        ),
    ]
