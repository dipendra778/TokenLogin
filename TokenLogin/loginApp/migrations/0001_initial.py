# Generated by Django 2.2.1 on 2019-05-28 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NestedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('speciality', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LoginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('phone', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=20)),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.NestedModel')),
            ],
        ),
    ]
