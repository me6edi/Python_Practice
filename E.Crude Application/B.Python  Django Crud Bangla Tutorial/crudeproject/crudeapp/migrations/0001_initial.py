# Generated by Django 3.0.5 on 2020-04-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inserting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('mname', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
            ],
        ),
    ]