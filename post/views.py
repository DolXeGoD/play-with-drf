from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import PostSerializer
from .models import Post

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get(self, request, pk):
        try:
            post =  Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def put(self, request, pk):
        try:
            post =  Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        try:
            post =  Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        