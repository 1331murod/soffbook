# Generated by Django 4.2.7 on 2023-11-30 11:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name="Avtorning to'liq ismi")),
                ('image', models.ImageField(upload_to='images/', verbose_name='Avtor rasmi')),
                ('bio', models.TextField(verbose_name="Author haqida ma'lumot")),
                ('country', models.CharField(max_length=200, verbose_name='Mamlakati')),
                ('birth_date', models.PositiveIntegerField(verbose_name="Tug'ulgan sanasi")),
                ('death_date', models.PositiveIntegerField(verbose_name='Vafot etgan sanasi')),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ganre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^\\+998\\d{9}$')])),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='images/', verbose_name='Kitob muqovasi')),
                ('pages', models.IntegerField(verbose_name='Varoqlar soni')),
                ('published', models.PositiveIntegerField(verbose_name='Nashr qilingan sanasi')),
                ('price', models.PositiveIntegerField(verbose_name='kitob narxi')),
                ('description', models.TextField()),
                ('order', models.IntegerField(default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.authors')),
                ('ganre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.ganre')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='authors',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.period'),
        ),
    ]
