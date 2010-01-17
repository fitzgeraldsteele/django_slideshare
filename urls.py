from django.conf.urls.defaults import *
from presentations.urls import *
from presentations.slideshare import views


urlpatterns = patterns('',
    # Example:
    (r'^(?P<object_id>\d+)/', views.show ),
    (r'^demo/', views.demo ),
    (r'^about/$', views.about ),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

