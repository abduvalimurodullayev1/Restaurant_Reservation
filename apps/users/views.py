from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import LoginSerializer  
from apps.users.serializers import RegisterSerializer
from rest_framework.response import Response

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer,
                         responses={201: RegisterSerializer})
    def post(self, request):
        serializers = RegisterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: "Login successfully",
            status.HTTP_400_BAD_REQUEST: "Invalid Credentials",
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.data.get('phone_number')
            password = serializer.data.get('password')
            user = authenticate(username=phone_number, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    "detail": "Successfully login",
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }, status=status.HTTP_200_OK)
            return Response({"detail": "Invalid phone number or password"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"detail": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)
