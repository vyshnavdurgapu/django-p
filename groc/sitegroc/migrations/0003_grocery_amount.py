# Generated by Django 4.1.3 on 2022-12-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitegroc', '0002_rename_quantity_grocery_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
