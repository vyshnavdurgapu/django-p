# Generated by Django 4.1.3 on 2022-12-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('o', 'oil'), ('g', 'grain'), ('c', 'cosmetics')], max_length=1)),
                ('Quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        ),
    ]