from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='sign_up'),
    path('usertype/', views.usertype, name='user_type'),
    path('studentinfo/', views.student_info, name='student_info'),
    path('supervisorinfo/', views.supervisor_info, name='supervisor_info'),
    path('administratorinfo/', views.administrator_info, name='admin_info'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/supervisor/', views.super_dashboard, name='super_dashboard'),
    path('rank/areaofinterest/', views.rankarea, name='rank_area'),
    path('rank/areaofinterest/', views.updaterankarea, name='up_rank_area'),
    path('dashboard/', views.dashboard, name='dashboard'),

    #admin paths

    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/admin/allocate', views.allocate, name='allocate'),
    path('dashboard/admin/results', views.allocate_results, name='allocate_results'),
    path('dashboard/admin/add/students', views.add_students, name='add_students'),
    path('dashboard/admin/add/supervisors', views.add_supervisors, name='add_supervisors'),
    path('dashboard/admin/add/deadline', views.reg_deadline, name='reg_deadline'),
    path('dashboard/admin/students', views.total_students, name='total_students'),
    path('dashboard/admin/supervisors', views.total_supervisors, name='total_supervisors'),
    path('dashboard/admin/unallocated/students', views.unallocated_students, name='unallocated_students'),
    path('dashboard/admin/unallocated/supervisors', views.unallocated_supervisors, name='unallocated_supervisors'),
    path('dashboard/admin/unallocated/students', views.set_contraints, name='set_contraints'),
]