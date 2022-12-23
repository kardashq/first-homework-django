from django.contrib import admin

from miniapp.models import Category, Event


# admin.site.register(Category)
# admin.site.register(Event)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
