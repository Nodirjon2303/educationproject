# Generated by Django 3.2.9 on 2021-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0003_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
