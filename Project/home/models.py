from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Work(models.Model):
    fname = models.CharField(max_length=122)
    lname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    resume = models.FileField(upload_to=None, max_length=254,)
    add = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.fname
    