from django.urls import path
from . import views

urlpatterns = [ 
    path('mainjourn/', views.add_sjourn, name='add_sjourn'),
    path('mainjourn_view/', views.view_sjourn, name='view_sjourn'),
    path('mainjourn_remove/<str:pk_test>/', views.remove_sjourn, name='remove_sjourn'),

    path('rjourn/', views.add_rjourn, name='add_rjourn' ),
    path('view_rjourn/<str:pk_test>/', views.view_rjourn, name='view_rjourn'),
    path('edit_rjourn/<str:pk_test>/', views.edit_rjourn, name='edit_rjourn'),
    path('remove_rjourn/<str:pk_test>/', views.remove_rjourn, name='remove_rjourn'),

    path('journal/', views.add_journal, name='add_journal' ),
    path('edit_journal/<str:pk_test>/', views.edit_journ, name='edit_journ'),
     path('remove_journal/<str:pk_test>/', views.remove_journ, name='remove_journal'),


    path('view_journ/<str:pk_test>/', views.view_myjournal, name='view_myjourn'),
   
    path('journaldr/<str:pk_test>/', views.add_journdr, name='add_journdr' ),
    path('remove_journdr/<str:pk_test>/', views.remove_journdr, name='remove_journdr'),
    path('edit_journdr/<str:pk_test>/', views.edit_journdr, name='edit_journdr'),


]