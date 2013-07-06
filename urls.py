from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.article_view'),
    url(r'^archive/', include('blog.urls')),
    url(r'^projects/', 'crane.views.projects'),
    url(r'^about/', 'crane.views.about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*/$', 'crane.views.error404'),
)
