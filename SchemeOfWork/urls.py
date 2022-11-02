from django.urls import path
from . import views

urlpatterns = [ 
    path('scheme/add_main_scheme/', views.add_mainscheme, name='add_main_scheme'),
    path('scheme/view_main_scheme/', views.view_mscheme, name='view_main_scheme'),
    path('scheme/remove_mscheme/<str:pk_test>/', views.remove_mscheme, name='remove_main_scheme'),


    path('scheme/add_scheme/<str:pk_test>', views.add_scheme, name='add_scheme'),
    path('scheme/view_scheme/<str:pk_test>/', views.view_scheme, name='view_scheme'),
    path('scheme/edit_scheme/<str:id>/', views.edit_scheme, name='edit_scheme'),
    path('scheme/delete_scheme/<str:id>/', views.remove_scheme, name='delete_scheme'),


 

]