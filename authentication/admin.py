from django.contrib import admin
from .models import User, Location
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass