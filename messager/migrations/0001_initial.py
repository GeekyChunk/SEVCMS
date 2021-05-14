# Generated by Django 3.0.5 on 2021-05-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=500)),
            ],
        ),
    ]
