# Generated by Django 3.0.5 on 2021-05-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_remove_profile_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prof',
            field=models.ImageField(default=None, upload_to='prof-img'),
        ),
    ]
