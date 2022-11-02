from django.urls import path
from . import views
urlpatterns = [ 
    path('logbook/add_logbook_serial/', views.add_logbookserial, name='add_logbook_serial'),
    path('logbook/view_logbook_serial/', views.view_logbookserial, name='view_logbook_serial'),
    path('logbook/remove_logbook_serial/<str:pk_test>/', views.remove_logbookserial, name='remove_logbook_serial'),


    path('logbook/add_logbook/<str:pk_test>/', views.add_logbook, name='add_logbook'),
    path('logbook/view_logbook/<str:pk_test>/', views.view_logbook, name='view_logbook'),
    path('logbook/edit_logbook/<str:id>/', views.edit_logbook, name='edit_logbook'),
    path('logbook/remove_logbook/<str:id>/', views.remove_logbook, name='remove_logbook'),

]