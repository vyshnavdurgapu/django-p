# Generated by Django 4.1.3 on 2022-12-09 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitegroc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grocery',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
