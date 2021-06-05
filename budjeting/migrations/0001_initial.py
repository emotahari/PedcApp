# Generated by Django 3.2.4 on 2021-06-05 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currencyName', models.CharField(max_length=100, verbose_name='نام ارز')),
            ],
            options={
                'verbose_name': 'ارز',
                'verbose_name_plural': 'ارز',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='budjeting.currency')),
            ],
            options={
                'verbose_name': 'درآمد',
            },
        ),
    ]
