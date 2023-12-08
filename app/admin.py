from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", )
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", )

@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name")
    search_fields = ("name", )

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name")
    search_fields = ("name", )
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", )
    list_display_links = ("id", "title")
    search_fields = ("title", )

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "country", "period", )
    list_display_links = ("id", "full_name", "country", "period")
    search_fields = ("full_name", "country", )
    list_filter = ( "period", )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "price", "ganre", )
    list_display_links = ("id", "title", "author", "price", "ganre", )
    search_fields = ("title", "author", )
    list_filter = ("price", "ganre", )
