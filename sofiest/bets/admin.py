from django.contrib import admin
from .models import Event, EventCategory, EventSubCategory, Variant, EventResult, Bet, BetVariant, EventStatus
from django.urls import reverse
from django.utils.http import urlencode

displayed_models = [EventCategory, EventSubCategory, EventResult, Bet, BetVariant]
admin.site.register(displayed_models)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'sub_category', 'active_due_date', 'date')


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'event')
    list_filter = ['event']


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
