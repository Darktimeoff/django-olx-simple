from django.contrib import admin
from ads.models import Ad, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    pass