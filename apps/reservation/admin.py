from django.contrib import admin
from django.db.models import JSONField
from .models import Restaurant, Reservation, User
from prettyjson.widgets import PrettyJSONWidget

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'average_rating', 'available_sites')  
    list_filter = ('average_rating', 'available_sites')  
    search_fields = ('title', 'address', 'description')  
    ordering = ('-average_rating',)  
    readonly_fields = ('average_rating', 'reviews')  
    formfield_overrides = {
        JSONField: {'widget': PrettyJSONWidget}  # JSON maydonlar uchun chiroyli editor
    }


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant', 'reservation_time', 'number_people')  
    list_filter = ('reservation_time', 'restaurant')  
    search_fields = ('user__phone_number', 'restaurant__title')  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_active', 'is_superuser', 'is_staff')  
    list_filter = ('is_active', 'is_staff')  
    search_fields = ('phone_number',)  
    ordering = ('phone_number',)  
