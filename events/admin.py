from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'max_slots', 'slots_filled', 'slots_available', 'is_full')
    list_filter = ('date',)
    search_fields = ('title', 'description')