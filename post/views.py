from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.permissions import IsOwnerPermission
from post.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    permission_classes = IsOwnerPermission,

    def update(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        if request.user == post.author:
            serializer = self.serializer_class(data=request.data, instance=post)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response(data={"message": "You cannot update this post"}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def partial_update(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        if request.user == post.author:
            serializer = self.serializer_class(data=request.data, instance=post, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            return Response(data={"message": "You cannot update this post"}, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
