# Generated by Django 3.0.5 on 2020-04-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgapp', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='event',
            field=models.CharField(default='birthday', max_length=15),
            preserve_default=False,
        ),
    ]
