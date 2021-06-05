from django import forms

class NewDriver(forms.Form):
        
        name = forms.CharField(max_length = 20,help_text='Your Name')
        state = forms.CharField(max_length = 10,help_text='Your State')
        dist = forms.CharField(max_length = 20,help_text='Your District')
        phone = forms.IntegerField(help_text='Your Phone')
        pincode = forms.IntegerField(help_text='Your Pincode')
        experience = forms.FloatField(help_text='Your Experince(in year)')
        fee = forms.IntegerField(help_text='Your Fee(per month)')
        vehicle = forms.CharField(help_text='choose the vehicle u drive')
