# Generated by Django 4.0.4 on 2022-05-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_faces'),
    ]

    operations = [
        migrations.DeleteModel(
            name='faces',
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.TextField(default='Username'),
        ),
    ]
