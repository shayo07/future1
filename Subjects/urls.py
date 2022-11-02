from django.urls import path 
from . import views

urlpatterns=[
    path('subject/add_subject/', views.add_somo, name='add_subject' ),
    path('subject/view_subject/', views.view_masomo, name='view_subject'),
    path('subject/view_subject/<str:pk_test>/', views.remove_somo, name='remove_somo'),


    path('subject/result/<str:pk_test>/', views.add_result, name='add_result'),
    path('subject/result_list/<str:pk_test>', views.view_result, name='result_list'),
    path('subject/edit_result/<str:pk_test>', views.edit_result, name='edit_result'),
    path('subject/remove_result/<str:pk_test>', views.remove_result, name='remove_result'),

    path('addtog/<str:pk_test>/', views.file_load_view, name='addtog'),
    path('importdata/', views.import_csv, name='importcsv'),
    
]