# Generated by Django 3.1.6 on 2021-02-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universitite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nomer', models.CharField(max_length=13)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
