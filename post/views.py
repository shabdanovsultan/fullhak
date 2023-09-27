from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import generics
import django_filters
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Post
import random


User = get_user_model()


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'delete', 'retrieve']

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']
    filterset_fields = ['title']


class PostCategorySearchView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = PostFilter


    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"user": ["Пользователь не аутентифицирован"]}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PostSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRecommendationsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        all_posts = Post.objects.all()
        random_posts = random.sample(list(all_posts), min(len(all_posts), 4))
        return random_posts
