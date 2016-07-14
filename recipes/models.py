# encoding utf-8

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
    """Category model"""
    name = models.CharField(u'Name', max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(u'Beschreibung', blank=True)

    class Meta:
        verbose_name = u'Kategorie'
        verbose_name_plural = u'Kategorien'

    def __unicode__(self):
        return self.name

class Recipe(models.Model):
    """Recipe model"""
    title = models.CharField(u'Titel', max_length=255)
    slug = models.SlugField(unique=True)
    ingredients = models.TextField(u'Zutaten',
                                   help_text=u'Eine Zutat pro Zeile angeben')
    preparation = models.TextField(u'Zubereitung')
    time_for_preparation = models.IntegerField(u'Zubereitungszeit',
                                               help_text=u'Zeit in Minuten angeben',
                                               blank=True, null=True)
    number_of_portions = models.PositiveIntegerField(u'Anzahl der Portionen')