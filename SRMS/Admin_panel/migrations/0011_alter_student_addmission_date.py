# Generated by Django 4.0.1 on 2022-02-07 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_panel', '0010_alter_student_student_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='addmission_date',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]