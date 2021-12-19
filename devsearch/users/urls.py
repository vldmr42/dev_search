from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('account/', views.user_account, name='account'),
    path('edit_account/', views.edit_account, name='edit_account'),

    path('create_skill/', views.create_skill, name='create_skill'),
    path('update_skill/<str:pk>/', views.update_skill, name='update_skill'),
    path('delete_skill/<str:pk>/', views.delete_skill, name='delete_skill'),

    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.view_message, name='message'),
    path('create_message/<str:pk>/', views.create_message, name='create_message'),

]
