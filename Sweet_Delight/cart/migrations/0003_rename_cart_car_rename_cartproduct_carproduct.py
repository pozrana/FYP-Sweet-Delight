# Generated by Django 4.0.3 on 2022-04-10 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_foodmenu_digital'),
        ('cart', '0002_alter_customer_joined_on'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='CartProduct',
            new_name='CarProduct',
        ),
    ]
