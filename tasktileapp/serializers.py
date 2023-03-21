from rest_framework import serializers 
from .models import Tile,Task


class MainTaskSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')
    class Meta:
        model=Task
        fields=['id','title','order','description','type','tile']

class PostPutTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['id','title','order','description','type','tile']


class MainTileSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    total_task=serializers.SerializerMethodField(method_name='get_total_task_count')
    tasks=MainTaskSerializer(many=True)
    launch_date=serializers.DateTimeField(read_only=True)

    def get_total_task_count(self,tile:Tile):
        return tile.tasks.count()
    

    class Meta:
        model = Tile
        fields = ['id', 'launch_date', 'status','total_task','tasks']


class PostPutTileSerializer(serializers.ModelSerializer):
    launch_date=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Tile
        fields=['id','launch_date','status']