from django.urls import path
from . import views

urlpatterns = [ 
    path('mainlplan/', views.add_stplan, name='add_stplan'),
    path('mainlplan_view/', views.view_stplan, name='view_stplan'),
    path('mainlplan_remove/<str:pk_test>/', views.remove_stplan, name='remove_stplan'),

    path('tlessonplan/', views.add_tplan, name='add_tplan' ),
    path('view_tlessonplan/<str:pk_test>/', views.view_tplan, name='view_tplan'),
    path('edit_tplan/<str:pk_test>/', views.edit_tplan, name='edit_tplan'),
    path('remove_tplan/<str:pk_test>/', views.remove_tplan, name='remove_tplan'),

    path('lessonplan/<str:pk_test>/', views.add_lessonplan, name='add_lplan' ),
    path('edit_lessonplan/<str:pk_test>/', views.edit_lessonplan, name='edit_lplan'),
    path('view_lessonplan/<str:pk_test>/', views.view_lessonplan, name='view_lessonplan'),
    path('remove_lessonplan/<str:pk_test>/', views.remove_lessonplan, name='remove_lplan'),

    path('lessondevelopment/<str:pk_test>/', views.add_lessondev, name='add_ldev' ),
    path('remove_lessondevelopment/<str:pk_test>/', views.remove_lessondev, name='remove_ldev'),
    path('edit_lessondevelopment/<str:pk_test>/', views.edit_lessondev, name='edit_ldev'),


    path('lessonevaluation/<str:pk_test>/', views.add_lessoneval, name='add_leval' ),
    path('remove_lessonevaluation/<str:pk_test>/', views.remove_lessoneval, name='remove_leval'),
    path('edit_lessonevaluation/<str:pk_test>/', views.edit_lessoneval, name='edit_leval'),
   
]