# Generated by Django 5.0 on 2023-12-14 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_phone_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to='employee/'),
        ),
    ]
