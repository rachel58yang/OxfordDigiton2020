# Generated by Django 3.0.3 on 2020-05-30 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='response',
            field=models.IntegerField(default=0),
        ),
    ]
