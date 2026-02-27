from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser


from .models import Discussion, Comment,Community
from .serializators import DiscussionSerializer, CommentSerializer, CommunitySerializer

class CRUD_Discussion(ModelViewSet): 
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    parser_classes = [MultiPartParser, FormParser]

class CRUD_Comment(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CRUD_Community(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


        
