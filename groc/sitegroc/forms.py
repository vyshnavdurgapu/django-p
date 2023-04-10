from django.forms import ModelForm
from .models import grocery

class gform(ModelForm):
    class Meta:
        model = grocery
        fields = ['Name','type','quantity','rate']