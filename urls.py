from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'crane.views.home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^resume/', 'crane.views.resume'),
    url(r'^contact/', 'crane.views.contact'),
    url(r'^portfolio/', 'crane.views.portfolio'),
    url(r'^admin/', include(admin.site.urls)),
)
