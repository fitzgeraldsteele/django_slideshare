from django.db import models
import datetime

# Create your models here.
class Slideshare(models.Model):
    """(What I want to be able to show and control from a slideshare presentation)"""
    title = models.CharField(blank=False, max_length=100)
    url = models.URLField(blank=False, verify_exists=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    abstract = models.TextField(blank=True)
    date_posted = models.DateField("Date Posted", default=datetime.datetime.today)
    
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.title
