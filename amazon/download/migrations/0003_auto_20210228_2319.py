# Generated by Django 3.1.1 on 2021-03-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('download', '0002_auto_20210228_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asin_task',
            name='asin_name_list',
            field=models.CharField(default='a1-', max_length=63),
        ),
        migrations.AlterField(
            model_name='asin_task',
            name='request_description',
            field=models.CharField(default='b1-', max_length=63),
        ),
    ]