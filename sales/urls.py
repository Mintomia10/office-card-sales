from django.urls import path
from . import views


urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    # User CRUD
    path('users/', views.user_list, name='user_list'),
    path('users/add/', views.user_create, name='user_create'),
    path('users/edit/<int:id>/', views.user_update, name='user_update'),
    path('users/delete/<int:id>/', views.user_delete, name='user_delete'),

    # Sale CRUD
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/add/', views.sale_create, name='sale_create'),
    path('sales/edit/<int:id>/', views.sale_update, name='sale_update'),
    path('sales/delete/<int:id>/', views.sale_delete, name='sale_delete'),
]