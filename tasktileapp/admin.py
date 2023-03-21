from django.contrib import admin
from .models import Task,Tile
# Register your models here.

admin.site.index_title='Admin'
admin.site.site_header='Task Tile Admin'

class TaskInline(admin.TabularInline):
    model=Task
    extra=0

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['title','order','description','type','tile']
    list_per_page=10
    list_filter=['type','tile']
    list_editable=['type']
    ordering=['title']
    list_select_related=['tile']
    search_fields=['title__icontains']
    search_help_text=('Search by title')

@admin.register(Tile)
class TileAdmin(admin.ModelAdmin):
    list_display=['launch_date','status', 'total_task']
    list_per_page=10
    list_filter=['status']
    list_editable=['status']
    ordering=['launch_date']
    inlines=[TaskInline]
    

    def total_task(self,tile:Tile):
        return tile.tasks.count()