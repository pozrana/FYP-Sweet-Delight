# Generated by Django 4.0.3 on 2022-04-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
