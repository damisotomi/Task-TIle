from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Tile(models.Model):
    
    # STATUS_CHOICES_LIVE="L"
    # STATUS_CHOICES_PENDING="P"
    # STATUS_CHOICES_ARCHIVED="A"

    STATUS_CHOICES=[
        (1,"Live"),
        (2,"Pending"),
        (3,"Archived"),
    ]

    launch_date=models.DateTimeField(auto_now_add=True)
    status= models.IntegerField(choices=STATUS_CHOICES,default=2)
    
    class Meta:
        ordering=['launch_date']

    def __str__(self):
        return str(self.id)
    

class Task(models.Model):
    

    TYPE_CHOICES=[
        (1,"Survey"),
        (2,"Discussion"),
        (3,"Diary")
    ]
    
    title=models.CharField(max_length=255)
    order=models.IntegerField(validators=[MinValueValidator(1)])
    description=models.TextField(null=True, blank=True)
    type=models.IntegerField(choices=TYPE_CHOICES,null=True, blank=True)
    tile=models.ForeignKey(Tile,on_delete=models.RESTRICT,related_name="tasks")


    def __str__(self) -> str:
        return self.title