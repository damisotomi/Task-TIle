from .models import Task,Tile
from .filters import TaskFilter
from .pagination import DefaultPagination
from .serializers import PostPutTaskSerializer,MainTaskSerializer, MainTileSerializer,PostPutTileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class TileViewset(ModelViewSet):
    queryset=Tile.objects.all()
    
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return PostPutTileSerializer
        else:
            return MainTileSerializer
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.tasks:
            return Response({'error':'Can not be deleted as it contains one or more tasks'})
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

    filter_backends=[DjangoFilterBackend]
    filterset_fields=['status']
    pagination_class=DefaultPagination
    

class TaskViewset(ModelViewSet):
    queryset=Task.objects.all()
    def get_serializer_class(self):
        if self.request.method=='POST' or self.request.method=='PUT':
            return PostPutTaskSerializer
        else:
            return MainTaskSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class=TaskFilter
    search_fields=['title']
    pagination_class=DefaultPagination