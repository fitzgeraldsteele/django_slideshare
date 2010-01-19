from presentations.slideshare.models import Slideshare
from django.contrib import admin

class SlideshareAdmin(admin.ModelAdmin):
    """Admin class for Slideshare.  """
    fieldsets = (
        (None, {
            'fields': ('title', 'url', 'width', 'height', 'abstract', 'date_posted')
        }),
        ('Advanced Settings', {
            'classes': ('collapse',),
            'fields': ('presentationurl', 'thumbnailurl', 'creator')
        }),
    )
        
admin.site.register(Slideshare, SlideshareAdmin)
        