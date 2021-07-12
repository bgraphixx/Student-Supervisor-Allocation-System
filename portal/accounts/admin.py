from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    ordering = ('user', )
    list_display = ("user" , "user_type", "gender", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("user_type", "gender")

class AreaOfInterestsAdmin(admin.ModelAdmin):
    ordering = ('user', )
    list_display = ("user" , "type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice",)

admin.site.register(Test)
admin.site.register(Profiles, ProfileAdmin)
admin.site.register(AreaOfInterests, AreaOfInterestsAdmin)