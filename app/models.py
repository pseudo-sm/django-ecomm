from django.db import models

# Create your models here.
class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    cod = models.BooleanField()
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to="product/")
    def __str__(self):
        return self.name+" - "+str(self.id)
