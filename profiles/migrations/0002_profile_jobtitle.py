# Generated by Django 5.1.2 on 2024-11-16 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='jobtitle',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
