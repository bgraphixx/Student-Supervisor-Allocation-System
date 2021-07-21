from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("user" , "user_type", "gender", ) #Set display in admin to list these columns
    search_fields = ("user", ) #Create a search box to search these fields 
    list_filter = ("user_type", "gender")

class StudentsAreaOfInterestsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("student" , "type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice", ) #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 
    list_filter = ("type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice",)

class SupervisorsAreaOfInterestsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("supervisor" , "type", "first_choice","second_choice","third_choice","fourth_choice","fifth_choice", ) #Set display in admin to list these columns
    search_fields = ("supervisor", ) #Create a search box to search these fields 
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
    
class AdministratorsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("staff" , "staff_level", "department") #Set display in admin to list these columns
    search_fields = ("staff", ) #Create a search box to search these fields 
    list_filter = ("staff_level", "department")

class AllocatedAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("student", "supervisor") #Set display in admin to list these columns
    search_fields = ("student", "supervisor") #Create a search box to search these fields 

# class StudentRankingAdmin(admin.ModelAdmin):
#     ordering = ('id', )
#     list_display = ("student", "first_choice", "second_choice", "third_choice", "fourth_choice", "fifth_choice") #Set display in admin to list these columns
#     search_fields = ("student",) #Create a search box to search these fields 

# class SupervisorRankingAdmin(admin.ModelAdmin):
#     ordering = ('id', )
#     list_display = ("supervisor", "first_choice", "second_choice", "third_choice", "fourth_choice", "fifth_choice") #Set display in admin to list these columns
#     search_fields = ("supervisor",) #Create a search box to search these fields 

class UnallocatedStudentsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("student", "level", "department", "course") #Set display in admin to list these columns
    search_fields = ("student", ) #Create a search box to search these fields 

class UnallocatedSupervisorsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("supervisor", "staff_level", "department" ) #Set display in admin to list these columns
    search_fields = ("supervisor", ) #Create a search box to search these fields 

class SupervisorConstraintsAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ("id", "professor","assoc_professor", "senior_lect", "lect_one", "lect_two", "assist") #Set display in admin to list these columns

class RegDeadlineAdmin(admin.ModelAdmin):
    ordering = ('id', )
    list_display = ('area_of_interest', 'ranking', 'submit_profile', 'allocation_result')


admin.site.register(Profiles, ProfileAdmin)
admin.site.register(StudentsAreaOfInterests, StudentsAreaOfInterestsAdmin)
admin.site.register(SupervisorsAreaOfInterests, SupervisorsAreaOfInterestsAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Supervisors, SupervisorsAdmin)
admin.site.register(Administrators, AdministratorsAdmin)
# admin.site.register(StudentRanking, StudentRankingAdmin)
# admin.site.register(SupervisorRanking, SupervisorRankingAdmin)
admin.site.register(UnallocatedStudents, UnallocatedStudentsAdmin)
admin.site.register(UnallocatedSupervisors, UnallocatedSupervisorsAdmin)
admin.site.register(Allocated, AllocatedAdmin)
admin.site.register(SupervisorContraints, SupervisorConstraintsAdmin)
admin.site.register(RegDeadline, RegDeadlineAdmin)
