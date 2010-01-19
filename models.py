from django.db import models
from django.db.models.signals import pre_save
import datetime

# Create your models here.
class Slideshare(models.Model):
    """(What I want to be able to show and control from a slideshare presentation)"""
    title = models.CharField(blank=True, max_length=100)
    url = models.URLField(blank=False, verify_exists=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    abstract = models.TextField(blank=True)
    date_posted = models.DateField("Date Posted", default=datetime.datetime.today)
    
    presentationurl = models.URLField(blank=True, verify_exists=True)
    thumbnailurl = models.URLField(blank=True, verify_exists=True)
    creator = models.CharField(blank=True, max_length=100)
    #postedtoslideshare = models.DateField(default=datetime.datetime.today)
    
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.title
        

def getpresentationdetails(sender, **kwargs):
    print "Pre Save!"
    #print sender
    model =  kwargs['instance']
    
    
    # fetch the presentation url
    
    try:
        import urllib
        from BeautifulSoup import BeautifulSoup as BS
        html = urllib.urlopen(kwargs['instance'].url).read()
        bs = BS(html)
        # find the let's get the media url

        presurl = bs.find('link', rel='media:presentation')
        print "* Presentation: " + presurl['href']
        # and the thumbnail
        thumburl = bs.find('link', rel='image_src')
        print "* Thumbnail: " + thumburl['href']
        # and the author ame
        creator = bs.find('meta', property='dc:creator')
        print "* Creator: " + creator['content']
        
        title = bs.find('meta', property="media:title")
        print "* Content: " + title['content']

    except Exception, e:
        raise e
    else:
        model.presentationurl = presurl['href']
        model.thumbnailurl = thumburl['href']
        model.creator = creator['content']
        
        if not model.title:
            model.title = title['content']
            
        if not model.width:
            model.width = bs.find('meta', property="media:width")['content']
            
        if not model.height:
            model.height = bs.find('meta', property="media:height")['content']

# Register callback for presave
pre_save.connect(getpresentationdetails, sender=Slideshare)