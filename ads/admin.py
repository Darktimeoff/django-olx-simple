from django.contrib import admin
from ads.models import Ad, Category, User, Location

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass