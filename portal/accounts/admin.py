from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "user" , "user_type", "gender", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("user_type", "gender")

admin.site.register(Test)
admin.site.register(Profile, ProfileAdmin)