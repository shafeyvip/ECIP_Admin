# Generated by Django 5.0 on 2024-06-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_ticket_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_code',
            field=models.IntegerField(auto_created=True, default=1000),
        ),
    ]
