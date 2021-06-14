# Generated by Django 3.2.4 on 2021-06-12 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('budgeting', '0003_auto_20210606_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='accounts.company'),
        ),
        migrations.AddField(
            model_name='income',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='budgeting.currency'),
        ),
        migrations.AlterField(
            model_name='income',
            name='projectName',
            field=models.CharField(max_length=100, null=True, verbose_name='نام محصول/خدمت درامدی'),
        ),
    ]
