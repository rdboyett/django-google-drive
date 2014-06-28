from django.conf.urls import patterns, include, url


urlpatterns = patterns('google_drive.views',
    (r'^pickFile/$', 'google_picker'),    
)
