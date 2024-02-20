# Generated by Django 5.0.1 on 2024-02-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
