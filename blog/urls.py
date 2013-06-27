from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title = "L. Gabriel Miller"
    description = "Ramblings of Gabe Miller"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-created")
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u"/blog/%d" % item.id #update url

urlpatterns = patterns('blog.views',
    url(r'^$', 'bloglist'),
    url(r'^feed/$', BlogFeed()),
    url(r'^pk/(?P<pk>\d+)$', 'pkview'),
    url(r'^post/(?P<slug>[\w-]+)$','postview'),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
)
