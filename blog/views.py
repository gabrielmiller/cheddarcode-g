from blog.models import Post
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

today = datetime.today().year

def article_view(request, year=None, slug=None):
    if year == None:
        post = Post.objects.all().order_by('-created')[0]
        return render_to_response("post.html", dict(post=post, page="blog", year=today))
    else:
        try:
            min_date = "%s-01-01" % year
            max_date = "%s-12-31" % year
            post = Post.objects.all().filter(created__lte=max_date, created__gte=min_date).get(slug=slug)
            return render_to_response("post.html", dict(post=post, page="archive", year=today))
        except:
            return render_to_response("404.html", dict(resource="blog post", year=today))

def archive_view(request):
    tags = Post.tags.all()
    posts = Post.objects.all().order_by('-created')
    return render_to_response("archive.html", dict(tags=tags, posts=posts, page="archive", year=today))

def tag_view(request, tag):
    posts = Post.objects.all().order_by('-created').filter(tags__name=tag)
    tags = Post.tags.all()
    return render_to_response("archive.html", dict(tag=tag, tags=tags, posts=posts, page="archive", year=today))
