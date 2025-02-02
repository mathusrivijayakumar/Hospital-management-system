# Generated by Django 4.1.3 on 2023-10-29 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_remove_details_country_remove_details_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('docid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('docname', models.CharField(max_length=40)),
                ('specialisation', models.CharField(max_length=40)),
                ('docemail', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=25)),
                ('contact', models.BigIntegerField()),
                ('address', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appid', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('appdate', models.DateTimeField()),
                ('apptime', models.TimeField()),
                ('docid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.doctors')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.details')),
            ],
        ),
    ]
