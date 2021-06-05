from django import forms

class NewCp(forms.Form):
    name = forms.CharField(max_length = 20,help_text='Your Name:')
    state = forms.CharField(max_length = 10,label='state',help_text='Your State:')
    dist = forms.CharField(max_length = 20,label='district',help_text='Your District:')
    phone = forms.IntegerField(label='phone',help_text='Your phone no.:')
    pincode = forms.IntegerField(label='pincode',help_text='Your Pincode:')
    experience = forms.FloatField(label='experience',help_text='Your Experince(in years):')
    fee = forms.IntegerField(label='fee',help_text='Your Fee(per day):')
