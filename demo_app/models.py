from django.db import models
import uuid

# Create your models here.

class Entry(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=40,null=True)
    address = models.CharField(max_length=80,null=True)
    contact = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Entries"    
        

