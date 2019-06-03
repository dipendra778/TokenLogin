from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import LoginModel,NestedModel
from .serializers import LoginSerializer,NestedSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly

# Create your views here.

class LoginViewSet(viewsets.ModelViewSet):
    queryset = LoginModel.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [IsAdminUser]


class NestedViewSet(viewsets.ModelViewSet):
    queryset = NestedModel.objects.all()
    serializer_class = NestedSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

