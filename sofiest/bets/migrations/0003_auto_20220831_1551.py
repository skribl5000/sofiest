# Generated by Django 3.0 on 2022-08-31 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0002_auto_20220831_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='variants',
        ),
        migrations.AddField(
            model_name='variant',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Event'),
        ),
    ]
