from .serializers import SoftDeskTokenObtainPairSerializer, SignupSerializer

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class SoftDeskObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = SoftDeskTokenObtainPairSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer