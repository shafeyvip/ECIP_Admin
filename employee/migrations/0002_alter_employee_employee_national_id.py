# Generated by Django 5.0 on 2023-12-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_national_id',
            field=models.IntegerField(),
        ),
    ]
