# Generated by Django 2.1.2 on 2018-10-30 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20181018_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board', to='base.Board'),
        ),
    ]
