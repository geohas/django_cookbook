# encoding utf-8

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


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
    DIFFICULTY_EASY = 1
    DIFFICULTY_MEDIUM = 2
    DIFFICULTY_HARD = 3
    DIFFICULTIES = (
        (DIFFICULTY_EASY, u'einfach'),
        (DIFFICULTY_MEDIUM, u'normal'),
        (DIFFICULTY_HARD, u'schwer')
    )
    title = models.CharField(u'Titel', max_length=255)
    slug = models.SlugField(unique=True)
    ingredients = models.TextField(u'Zutaten',
                                   help_text=u'Eine Zutat pro Zeile angeben')
    preparation = models.TextField(u'Zubereitung')
    time_for_preparation = models.IntegerField(u'Zubereitungszeit',
                                               help_text=u'Zeit in Minuten angeben',
                                               blank=True, null=True)
    number_of_portions = models.PositiveIntegerField(u'Anzahl der Portionen')
    difficulty = models.SmallIntegerField(u'Schwierigkeitsgrad',
                                          choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
    category = models.ManyToManyField(Category, verbose_name=u'Kategorien')
    author = models.ForeignKey(User, verbose_name=u'Autor')
    date_created = models.DateTimeField(editable=False)
    date_updated = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = u'Rezept'
        verbose_name_plural = u'Rezepte'
        ordering = ['-date_created']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Recipe,self).save(*args, **kwargs)
