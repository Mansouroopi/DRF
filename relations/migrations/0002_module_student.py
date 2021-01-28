# Generated by Django 3.1.5 on 2021-01-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('length', models.IntegerField(verbose_name=20)),
                ('class_room', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('modules', models.ManyToManyField(to='relations.Module')),
            ],
        ),
    ]
