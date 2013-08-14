__author__ = 'gil'

from django.contrib import admin
from countsApp.models import Count,User

class CountInline(admin.TabularInline):
    model = Count
    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                   {'fields': ['name']}),
        ('Counts',               {'fields': ['email'],'classes': ['collapse']}),

    ]
    inlines = [CountInline]

admin.site.register(User,UserAdmin)