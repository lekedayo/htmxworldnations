from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name


class Subregion(models.Model):
    '''Model definition for subregion.'''
    name = models.CharField(max_length=250)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    class Meta:
        '''Meta definition for subregion.'''

        verbose_name = 'subregion'
        verbose_name_plural = 'subregions'

    def __str__(self):
        return f"{self.name}, {self.region}"
    

class Country(models.Model):
    '''Model definition for Country.'''
    name = models.CharField(max_length=250)
    subregion = models.ForeignKey(Subregion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countrys")

    def __str__(self):
        return f"{self.name}, {self.subregion}, {self.subregion.region}"


class State(models.Model):
    '''Model definition for state.'''
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return f"{self.name}, {self.country}, {self.country.subregion}, {self.country.subregion.region}"



class City(models.Model):
    '''Model definition for City.'''
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Citys")
    
    def __str__(self):
        return f"{self.name}, {self.state}, {self.state.country}, {self.state.country.subregion}, {self.state.country.subregion.region}"