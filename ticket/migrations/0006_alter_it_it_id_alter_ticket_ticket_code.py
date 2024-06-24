# Generated by Django 5.0 on 2024-06-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_new_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it',
            name='it_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_code',
            field=models.IntegerField(auto_created=True, default=1000, unique=True),
        ),
    ]
