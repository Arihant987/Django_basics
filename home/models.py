from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    date =  models.DateField()

    def __str__(self):
        return self.email