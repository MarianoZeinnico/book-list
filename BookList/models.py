# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
#from django.conf import settings

# Create your models here.
class Book(models.Model):
    idBook = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    datePublished = models.DateField()
    #input_formats=settings.DATE_INPUT_FORMATS
    numberOfPages = models.IntegerField()
    typeOfBook = models.CharField(max_length=50)

    def __unicode__(self):
        return ' '.join([
            self.idBook,
            self.title,
            self.author,
            self.datePublished,
            self.numberOfPages,
            self.typeOfBook,
        ])