# Generated by Django 3.1.1 on 2021-03-01 05:44

from django.db import migrations, models
import django.db.models.deletion
import download.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ASIN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ASIN_task',
            fields=[
                ('ASIN_task_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('asin_name_list', models.CharField(default='a1', max_length=63)),
                ('request_description', models.CharField(default='b1', max_length=63)),
                ('Start_time', models.DateField(default='')),
                ('End_time', models.DateField(default='')),
                ('request_status', models.CharField(default=download.models.Task_Status['ready'], max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_if', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1300)),
                ('clinic_name', models.CharField(max_length=1300)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('submitted_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ASIN_Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='download.asin')),
            ],
        ),
    ]
