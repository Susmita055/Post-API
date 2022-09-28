from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from attendencemanagementsystems.serializers import LoginSerializer, PostSerializer, UserRegisterSerializer, ContactDetailsSerializer, Post
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .permissions import Custompermission
from rest_framework import generics


# Create your views here.


class UserRegister(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Login(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token': token, 'message': 'Login SuccessFull'}, status=status.HTTP_200_OK)
        return Response({'message': 'Please enter a valid username and password'}, status=status.HTTP_400_BAD_REQUEST)


class PostCreateView(APIView):
    permission_class = [IsAuthenticated]

    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    # permission_classes = [permission, ]
    permission_classes = [Custompermission]

    def get_object(self, pk):

        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):

        if pk is not None:
            post = self.get_object(pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Create(GenericAPIView):
    serializer_class = PostSerializer
    posts = Post.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class List(generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)

    def get(self, request):

        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class Retrieve(generics.RetrieveAPIView):
    def get(self, request, pk):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
