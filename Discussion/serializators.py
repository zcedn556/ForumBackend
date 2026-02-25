from rest_framework import serializers
from .models import Discussion, Comment,Community

class DiscussionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Discussion
        fields = "__all__"  
        read_only_fields = ['dateTimeOfCreation']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['dateTimeOfCreation']

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"
        read_only_fields = ['dateTimeOfCreation']
        