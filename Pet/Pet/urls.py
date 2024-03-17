from django.contrib import admin
from django.urls import path
from ShopApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('veterinario/', views.login,name='veterinario'),
    path('servicos/', views.login,name='servicos'),
    
]
