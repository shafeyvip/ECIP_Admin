# Generated by Django 5.0 on 2023-12-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_employee_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_phone_1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_phone_2',
            field=models.IntegerField(),
        ),
    ]
