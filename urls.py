from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'crane.views.home'), # call article_view on most recent article
    url(r'^archive/', include('blog.urls')),
    url(r'^projects/', 'crane.views.projects'), #projects
    url(r'^about/', 'crane.views.about'), #about
    url(r'^admin/', include(admin.site.urls)),
    url(r'^./$', 'crane.views.404'), # 404
    #url(r'^blog/', include('blog.urls')), # archives?
    #url(r'^resume/', 'crane.views.resume'),
    #url(r'^contact/', 'crane.views.contact'),
    #url(r'^portfolio/', 'crane.views.portfolio'),
)
