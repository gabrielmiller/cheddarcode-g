from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
#from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'crane.views.home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^resume/', 'crane.views.resume'),
    url(r'^contact/', 'crane.views.contact'),
    url(r'^portfolio/', 'crane.views.portfolio'),
    #url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',{'url':'http://www.cheddarcode.com/g/favicon.ico'}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    staticfiles_urlpatterns(),
)
