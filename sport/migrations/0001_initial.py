
# Generated by Django 4.2.5 on 2023-09-09 12:55
import datetime
# Generated by Django 4.2.5 on 2023-09-09 12:43
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YangilikModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Y_nomi', models.CharField(default='', max_length=150)),
                ('Y_matni', models.CharField(default='', max_length=1300)),
                ('Y_vaxti', models.DateField(default=datetime.datetime.now)),
                ('Y_rasmi', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'yangilik',
            name='CoachModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50)),
                ('degvee', models.CharField(default='', max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='coach/')),
            ],
            options={
                'db_table': 'coach',
            },
        ),
    ]
