# Generated by Django 2.1.2 on 2018-11-11 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20181101_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Board'),
        ),
    ]
