from django.forms import ModelForm
from .models import *

class EzForm(ModelForm):
    class Meta:
        model=Ez
        fields=['title','ezFile']