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

class CountAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'count','changed_recently')
    list_filter = ['last_update']
    search_fields = ['name']

admin.site.register(User,UserAdmin)
admin.site.register(Count,CountAdmin)