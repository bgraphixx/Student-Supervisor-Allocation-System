from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('signup/', views.signup, name='sign_up'),
    path('usertype/', views.usertype, name='user_type'),
    path('studentinfo/', views.student_info, name='student_info'),
    path('supervisorinfo/', views.supervisor_info, name='supervisor_info'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/supervisor/', views.super_dashboard, name='super_dashboard'),
]