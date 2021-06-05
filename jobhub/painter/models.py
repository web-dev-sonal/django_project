from django.db import models

# Create your models here.
class painter(models.Model):
    name=models.CharField(max_length = 20)
    state=models.CharField(max_length = 10)
    dist=models.CharField(max_length = 20)
    phone=models.IntegerField()
    pincode=models.IntegerField()
    experience=models.FloatField()
    description=models.CharField(max_length = 200)
    fee=models.IntegerField()

    #class Meta:
     #   ordering = ['-experience','fee']

    def __str__(self):
        return self.name
