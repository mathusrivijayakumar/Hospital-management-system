# Generated by Django 4.2.6 on 2023-11-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0015_appointments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medrecord',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('docid', models.IntegerField()),
                ('docname', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('pid', models.IntegerField()),
                ('pname', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('bldgrp', models.CharField(max_length=5)),
                ('desc', models.CharField(max_length=150)),
                ('nxtapp', models.DateTimeField()),
                ('tplan', models.CharField(max_length=200)),
            ],
        ),
    ]
