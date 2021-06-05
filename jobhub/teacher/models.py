from django.db import models

# Create your models here.
class teacher(models.Model):
    math='math'
    physics='physics'
    chem='chemistry'
    bio='biology'
    cs='computer'
    en='english'

    subject_choice=(
        (math,'math'),
        (physics,'physics'),
        (chem,'chemistry'),
        (bio,'biology'),
        (cs,'computer'),
        (en,'english')
    )
    name=models.CharField(max_length = 20, help_text = 'enter your name')
    state=models.CharField(max_length = 10,help_text = 'enter your working state')
    dist=models.CharField(max_length = 20,help_text = 'enter your working district')
    phone=models.IntegerField(help_text = 'enter your contact no.')
    email=models.EmailField(help_text='enter your email id',null=True)
    pincode=models.IntegerField(help_text = 'enter your pin code')
    experience=models.FloatField(help_text = 'enter your work experince in year',)
    description=models.TextField(max_length=50,help_text='write about your teaching skill',null = True)
    subject=models.CharField(max_length=10,choices=subject_choice,help_text='which subject do you teach')
    fee=models.IntegerField(help_text='how much money(in rupees) you charge for one hour')

    #class Meta:
     #   ordering = ['-experience','fee']

    def __str__(self):
        return self.name
