from django.db import models

# Create your models here.
class Users(models.Model):
    """ class user """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    createdon = models.DateTimeField(auto_now_add=True)