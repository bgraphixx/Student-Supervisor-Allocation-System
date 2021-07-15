from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("user" , "user_type", "gender", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("user_type", "gender")

class AreaOfInterestsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("user" , "type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice",)

class StudentsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("student" , "level", "department", "course") #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 
    list_filter = ("level", "department", "course")

class SupervisorsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("staff" , "staff_level", "department") #Set display in admin to list these columns
    search_fields = ("staff", ) #Create a search box to search these fields 
    list_filter = ("staff_level", "department")

class AllocationAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("student" , "status", "supervisor") #Set display in admin to list these columns
    search_fields = ("student", "supervisor") #Create a search box to search these fields 
    list_filter = ("status", )

admin.site.register(Test)
admin.site.register(Profiles, ProfileAdmin)
admin.site.register(AreaOfInterests, AreaOfInterestsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Supervisors, SupervisorsAdmin)
admin.site.register(Allocation, AllocationAdmin)