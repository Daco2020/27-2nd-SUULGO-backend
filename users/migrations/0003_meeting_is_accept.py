# Generated by Django 4.0 on 2021-12-17 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_survey_alcohol_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='is_accept',
            field=models.BooleanField(default=False),
        ),
    ]
