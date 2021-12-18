from accounts.models import CustomUser
from accounts.api.serializers import UserSerializer
from rest_framework import viewsets


class CustomUserVeiwset(viewsets.ModelViewset):
    queryset = CustomUser.objects.all()
    serializers_class = UserSerializer
    
    