from apps.users.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'username', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        hash_password = make_password(password)  # type: ignore
        validated_data['password'] = hash_password
        return super().create(validated_data)
    


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            raise serializers.ValidationError("User not found")
        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password")
        return attrs
        
