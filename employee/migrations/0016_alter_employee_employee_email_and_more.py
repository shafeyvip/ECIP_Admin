# Generated by Django 5.0 on 2024-06-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0015_alter_employee_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_national_id',
            field=models.IntegerField(max_length=14),
        ),
        migrations.AlterField(
            model_name='employee',
            name='governorate',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]