from django.urls import path, include
from accounts.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.CustomUserViewSet, basename = 'CustomUser')
urlpatterns = [
    path('', include(router.urls))
]
