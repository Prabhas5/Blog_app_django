from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Post, Comment

class RegistrationSeralizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CommentSerializer(serializers.ModelSerializer):
    blog_title=serializers.CharField(source="post.title",read_only=True)
    class Meta:
        model = Comment
        fields = ['blog_title','text','created_date']
        read_only_fields=['created_date']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ['author','title','content','comments',]

    #creating one function to get author details
    def get_author(self,obj):
        return obj.author.username


    


