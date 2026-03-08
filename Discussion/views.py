from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Discussion, Comment,Community
from .serializators import DiscussionSerializer, CommentSerializer, CommunitySerializer

class CRUD_Discussion(ModelViewSet): 
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    parser_classes = [MultiPartParser, FormParser]

    @action(methods=['GET'], detail=True)
    def get_by_id(self,request,pk):
        comments = Comment.objects.filter(discussion_id = pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    
   
class CRUD_Comment(ModelViewSet):
    queryset = Comment.objects.all()    
    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticated]

class CRUD_Community(ModelViewSet): 
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

    @action(methods=['GET'], detail=True)
    def get_by_id(self,request,pk):
        discussions = Discussion.objects.filter(communityId_id = pk)
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)


        
