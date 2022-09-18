from django.db import models
from django.conf import settings


class EventCategory(models.Model):
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=256, verbose_name='Категория события')
    description = models.TextField(max_length=4000, verbose_name='Описание события', null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class EventSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=256, verbose_name='Подкатегория события')
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'


class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, default='')


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=128, null=True)
    title = models.CharField(max_length=256, verbose_name='Событие')
    description = models.TextField(max_length=4000, verbose_name='Описание события', null=True)
    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(EventSubCategory, on_delete=models.SET_NULL, null=True)
    active_due_date = models.DateTimeField(verbose_name='Дата закрытия прогноза')
    date = models.DateTimeField(verbose_name='Дата события')
    weight = models.FloatField(default=1, verbose_name='Значимость события')
    status = models.ForeignKey(EventStatus, on_delete=models.CASCADE, null=True, default=1)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Variant(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, verbose_name='Исход')
    description = models.TextField(max_length=4000, verbose_name='Описание исхода', null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}'


class EventResult(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, null=True)
    result = models.OneToOneField(Variant, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.event} - {self.result}'


class Bet(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, models.CASCADE)
    bet_maker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')

    objects = models.Manager()


class BetVariant(models.Model):
    id = models.AutoField(primary_key=True)
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    weight = models.FloatField(verbose_name='Вероятность исхода')

    objects = models.Manager()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, default='', null=True)
    text = models.TextField(max_length=4000, null=True, blank=False)
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)

    objects = models.Manager()


class CommentLike(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, default='', null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    objects = models.Manager()