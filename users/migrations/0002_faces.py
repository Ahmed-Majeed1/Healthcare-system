# Generated by Django 4.0.4 on 2022-05-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ImageField(upload_to='faces')),
            ],
        ),
    ]
