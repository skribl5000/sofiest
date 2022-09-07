# Generated by Django 3.0 on 2022-08-31 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=128, null=True)),
                ('title', models.CharField(max_length=256, verbose_name='Событие')),
                ('description', models.TextField(max_length=4000, null=True, verbose_name='Описание события')),
                ('active_due_date', models.DateTimeField(verbose_name='Дата закрытия прогноза')),
                ('date', models.DateTimeField(verbose_name='Дата события')),
                ('weight', models.FloatField(default=1, verbose_name='Значимость события')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=128, null=True)),
                ('name', models.CharField(max_length=256, verbose_name='Категория события')),
                ('description', models.TextField(max_length=4000, null=True, verbose_name='Описание события')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Исход')),
                ('description', models.TextField(max_length=4000, null=True, verbose_name='Описание исхода')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='bets.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=128, null=True)),
                ('name', models.CharField(max_length=256, verbose_name='Подкатегория события')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bets.EventCategory')),
            ],
        ),
        migrations.CreateModel(
            name='EventResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Event')),
                ('result', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Variant')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bets.EventCategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='bets.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bets.EventSubCategory'),
        ),
        migrations.CreateModel(
            name='BetVariant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.FloatField(verbose_name='Вероятность исхода')),
                ('bet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Event')),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bets.Variant')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bet_maker', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bets.Event')),
            ],
        ),
    ]