from django import forms
from .models import *

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class SubregionForm(forms.ModelForm):
    class Meta:
        model = Subregion
        fields = '__all__'

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'