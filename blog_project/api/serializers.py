from rest_framework import serializers
from .models import User, Story, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']  
        extra_kwargs = {'password': {'write_only': True}}  

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'] 
        )
        return user  
    
    
class StorySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'author', 'section', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    story = StorySerializer(read_only=True)

    class Meta:
        model = Comment    
        fields = ['id', 'user', 'story', 'content', 'created_at']




