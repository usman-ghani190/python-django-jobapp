from pydoc import classname
from django.db import models

# Create your models here.

class Uploads(models.Model):
    image = models.ImageField(upload_to="images")
    description= models.CharField( max_length=200)


    def __str__(self):
            return self.description
    

class UploadFile(models.Model):
      file = models.FileField(upload_to='files')
      description= models.CharField(max_length=200)


      def __str__(self):
          return self.description
      
    
