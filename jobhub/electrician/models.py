from django.db import models

# Create your models here.
class electrician(models.Model):
    name=models.CharField(max_length = 20, help_text = 'enter your name')
    state=models.CharField(max_length = 10,help_text = 'enter your working state')
    dist=models.CharField(max_length = 20,help_text = 'enter your working district')
    phone=models.IntegerField(help_text = 'enter your contact no.')
    pincode=models.IntegerField(help_text = 'enter your pin code',)
    experience=models.FloatField(help_text = 'enter your work experince in year',)
    fee = models.IntegerField(help_text='how much money(in rupees) you charge for one hour')

    #class Meta:
     #   ordering = ['-experience','fee']

    def __str__(self):
        return self.name
