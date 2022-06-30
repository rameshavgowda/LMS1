from django.urls import path, include
from core.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.Bookviewset, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
