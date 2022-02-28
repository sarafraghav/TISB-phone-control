from django.db import models

# Create your models here.

class signin(models.Model):
    cid = models.CharField(max_length=1000)
    signin = models.DateTimeField(auto_now_add=True)
    signout = models.DateTimeField(null=True)
    signedin = models.BooleanField()

    def __str__(self):
        return self.cid 

