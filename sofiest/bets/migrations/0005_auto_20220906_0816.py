# Generated by Django 3.0 on 2022-09-06 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0004_auto_20220906_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.EventStatus'),
        ),
    ]
