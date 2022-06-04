from pyexpat import model
from django import forms
from django.forms import ModelForm
from . models import Contract_Model

class Contract_forms(ModelForm):
    class Meta:
        model = Contract_Model
        fields = "__all__"


