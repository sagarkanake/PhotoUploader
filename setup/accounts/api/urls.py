from django.urls import path, include
from accounts.api import views
from rest_framework.routers import DefaultRouters

router = DefaultRouters()
router.register('crud', views.CustomUserVeiwset, basename = 'CustomUser')
urlpatterns = [
    path('', include(router.urls))
]
