from django.db import models
from django.utils import timezone   

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    date = models.DateField(default=timezone.now)
    desactivate = models.BooleanField(default=False)
    image = models.ImageField(default= 'static/img/adopta.jpg',upload_to='media/images_news/', null=True)
    category = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    mail = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    phone = models.BigIntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Denuncia(models.Model):
    direccion = models.CharField(max_length=100, null=True, unique=True)
    texto_denuncia = models.TextField(max_length=300)
    fecha_pub = models.DateTimeField(default=timezone.now)
    email = models.EmailField(null=True, unique=True)
    telefono = models.BigIntegerField(null=True, unique=True)        

