from django.contrib import admin
from .models import Table, Booking
# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'location', 'is_active')
    list_filter = ('capacity', 'is_active')
    search_fields = ('number', 'location')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'table', 'date', 'time', 'guests', 'is_cancelled')
    list_filter = ('date', 'is_cancelled')
    search_fields = ('user__username', 'table__number')
    date_hierarchy = 'date'