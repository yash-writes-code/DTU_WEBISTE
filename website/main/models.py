from django.db import models
import datetime
# Create your models here.
class Article(models.Model):
    descr=models.CharField(max_length=100)
    file=models.FileField(upload_to="uploads/")
    uploaded_at=models.DateField(auto_now_add=True)
                    
    def __str__(self):
        return self.descr
