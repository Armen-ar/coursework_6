from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from . import permissions
from rest_framework.decorators import action

from .models import Ad, Comment
from ads.filters import AdFilter
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_classes = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'me']:
            self.permission_classes = [permissions.IsAdmin]
        else:
            self.permission_classes = [permissions.IsAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_instance = get_object_or_404(Ad, id=self.kwargs['ad_pk'])
        return ad_instance.ads.all()

    def perform_create(self, serializer):
        ad_instance = get_object_or_404(Ad, id=self.kwargs['ad_pk'])
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
