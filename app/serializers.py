from rest_framework import serializers
from django.contrib.auth import get_user_model

from app.models import Status


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'first_name', 'last_name', 
            'country_code', 'phone_number', 'gender',
            'birthdate', 'avatar', 'email', 'password'
        )
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6},
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserStatusSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Status
        fields = ('id', 'user', 'status')
