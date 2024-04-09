from django.contrib import admin
from django.urls import path
from ShopApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('cadastro/', views.cadastro,name='cadastro'),
    path('veterinario/', views.veterinario, name='veterinario'),
    path('agenda/', views.agenda, name='agenda'),
    path('salvar/', views.salvar, name="salvar"),
]
