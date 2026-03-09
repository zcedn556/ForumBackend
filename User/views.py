from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializators import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action    
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def profile(self, request):
        user = request.user

        return Response({
            "id": user.id,
            "username": user.username
        })
    