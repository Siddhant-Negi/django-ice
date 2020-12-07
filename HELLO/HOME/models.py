from django.db import models
#makemigrations will store the changes in file
#migration will apply the changes to the database which was  done by makemigrations
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
class Transaction(models.Model):
    Name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.TextField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    zipp=models.CharField(max_length=10)
    Flavour=models.CharField(max_length=20)
    Price=models.CharField(max_length=3)
    Qty=models.CharField(max_length=3)
    Amount=models.CharField(max_length=4)
    Payment=models.CharField(max_length=20)
    date=models.DateField()


# Create your models here.
