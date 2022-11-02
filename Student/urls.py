from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    
    path('home/', views.index, name='home'),


    path('', views.log_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('view_teacher/', views.teachers, name='teachers'),
    path('edit_profile/<str:pk_test>/', views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<str:pk_test>/', views.teachers, name='delete_teacher'),
    path('add_profile/', views.add_teacher, name='add_teacher'),


    path('add_student/', views.add_student, name='add_student' ),
    path('view_student/', views.view_students, name='view_student'),
    path('student_details/<str:pk_test>/', views.student_details, name='student_details'),
    path('edit_student/<str:pk_test>/', views.edit_student, name='edit_student'),
    path('delete_student/<str:pk_test>/', views.remove_student, name='delete_student'),


    path('add_classes/', views.add_classes, name='add_classes'),
    path('view_classes/', views.view_classes, name='view_classes'),
    path('view_classes/<str:pk_test>/', views.class_details, name='class_details'),
    path('delete-class/<str:pk_test>/', views.remove_class, name='delete_class'),
    #path('edit-class/<str:pk_test>/', views.edit_class, name='edit_class'),

    path('add_darasa/<str:pk_test>/', views.add_darasa, name='add_darasa'),
    path('view_student/<str:pk_test>/', views.view_cstudent, name='view_cstudent'),
    path('remove_student/<str:pk_test>/', views.remove_cstudent, name='remove_cstudent'),

    path('general_class_result/<pk_test>/', views.general_class_result, name='general_class_result'),
    path('student_result/<str:pk_test>/', views.student_result, name='student_result'),
    path('delete_gresult/<str:pk_test>/', views.remove_gresult, name='delete_gresult'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset1.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
