# Generated by Django 3.2.4 on 2021-06-05 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0002_auto_20210606_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='isInGroupe',
            field=models.BooleanField(default=0, verbose_name='درآمد درون گروهی'),
        ),
        migrations.AlterField(
            model_name='income',
            name='projectName',
            field=models.CharField(max_length=100, null=True, verbose_name='نام پروژه/خدمت درامدی'),
        ),
    ]
