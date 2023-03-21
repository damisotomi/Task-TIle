from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register('tiles',views.TileViewset)
router.register('tasks',views.TaskViewset)

urlpatterns=router.urls