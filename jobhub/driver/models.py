from django.db import models

# Create your models here.
class driver(models.Model):

    CAR='car'
    BIKE='bike'
    AUTO='auto'
    vehicle_choices = (
        (CAR,'car'),
        (BIKE,'bike'),
        (AUTO,'auto')
    )
    name = models.CharField(max_length = 20 , help_text = 'enter your name')
    state=models.CharField(max_length = 10 , help_text = 'enter your working state')
    dist=models.CharField(max_length = 20,help_text = 'enter your working district')
    phone=models.IntegerField(help_text = 'enter your contact no.')
    pincode=models.IntegerField(help_text = 'enter your pin code')
    experience=models.FloatField(help_text = 'enter your work experince in year')
    vehicle = models.CharField(max_length=5,choices=vehicle_choices , default=BIKE , help_text='choose the vehicle u drive')
    fee = models.IntegerField(help_text='how much money(in rupees) you charge for one day')

    #class Meta:
     #   ordering = ['-experience','fee']

    def __str__(self):
        return self.name
