# Generated by Django 5.0 on 2023-12-18 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_alter_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
