from accounts.models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password', 'first_name', 'last_name' ]
        