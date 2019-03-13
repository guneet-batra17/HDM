# Generated by Django 2.0.6 on 2019-02-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=225)),
                ('department_strength', models.IntegerField()),
                ('department_location', models.CharField(max_length=225)),
                ('department_head', models.CharField(max_length=225)),
            ],
        ),
    ]