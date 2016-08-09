from django import forms
from .models import Devices
from .models import EditLog 
from django.contrib.auth.models import User




class DevicesForm(forms.ModelForm):
    class Meta:
        model=Devices
        fields = ( 'name', 'serial_num', 'ip_addr','enable' )


class LogForm(forms.ModelForm):
    class Meta:
        model=EditLog
        fields =('writer','serial','update_date')

class JoinForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget= forms.PasswordInput())



