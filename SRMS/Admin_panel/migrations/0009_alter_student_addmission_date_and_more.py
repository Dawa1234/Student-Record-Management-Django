# Generated by Django 4.0.1 on 2022-02-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0008_alter_student_addmission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='addmission_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
