from blog_app.serializers import CommentSerializer,PostSerializer,RegistrationSeralizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import Http404
from . models import Comment,Post
from django.contrib.auth.models import User


class RegitrationAPIView(APIView):
    def post(self,request):
        serializer = RegistrationSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        # Fetch user data from request
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Generate or retrieve token for the user
            token, _ = Token.objects.get_or_create(user=user)

            # Send token to user in response
            return Response({'Token': token.key}, status=200)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)


class PostListCreateAPIView(APIView):    
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        #filter the data on the exiting User
        posts = Post.objects.filter(author=request.user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        data=request.data            
        serializer = PostSerializer(data=data)    
        if serializer.is_valid():            
            serializer.save(author=request.user)
            data=serializer.data
            #Ading author name to returned data           
            data['author']=request.user.username            
            return Response(data, status=status.HTTP_201_CREATED)       
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailUpdateDeleteAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk,author=self.request.user)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        data={"data":"SUCESS !!"}
        return Response(data,status=status.HTTP_204_NO_CONTENT)

class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes=[TokenAuthentication]

    def get_queryset(self, post_id):
        return Comment.objects.filter(post_id=post_id)

    def get(self, request, post_id):
        comments = self.get_queryset(post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id,format=None):
        data = request.data
        
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user,post_id=post_id)
            data=serializer.data
            data['author']=request.user.username
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#defefing an another class for view all blogs for Public
class PostListAPIView(APIView): 
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




