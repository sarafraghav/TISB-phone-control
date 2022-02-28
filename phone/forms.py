from django.forms import ModelForm, DateInput
from .models import *

#Signup Form 
class handler(ModelForm):
    class Meta:
        model = signin
        fields = ['cid']