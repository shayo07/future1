from django.urls import path
from . import views
urlpatterns = [ 
    path('add_schoolAttendance/', views.add_sattendance, name='add_sattendance' ),
    path('view_schoolAttendance/', views.view_sattendance, name='view_sattendance'),
    path('remove_sattendance/<str:pk_test>/', views.remove_sattendance, name='remove_sattendance'),

    path('add_Attendance/<str:pk_test>/', views.add_attendance, name='add_attendance' ),
    path('view_Attendance/<str:pk_test>/', views.view_attendance, name='view_attendance'),
    path('remove_attendance/<str:pk_test>/', views.remove_attendance, name='remove_attendance'),

]