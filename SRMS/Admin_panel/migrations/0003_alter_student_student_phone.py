# Generated by Django 4.0.1 on 2022-02-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0002_alter_student_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_phone',
            field=models.PositiveBigIntegerField(),
        ),
    ]
