from django.urls import path
from . import views

# /nome_do_app
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout, name='logout'),
    path('mines_hack/', views.mines_hack, name='mines_hack'),
]