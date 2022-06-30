from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.log_in, name='login'),
    path('main/', views.main, name='main'),
    path('delete/<int:id>', views.deletebook, name='deletebook'),
    path('update/<int:id>', views.updatebook, name='updatebook'),
    path('logout/', views.user_logout, name='logout'),
    # path('logout/', views.logout, name='logout')
]
