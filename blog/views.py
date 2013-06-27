from blog.models import Post
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
#from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

def article_view(request, year, slug):
    try:
        min_date = "%s-01-01" % year
        max_date = "%s-12-31" % year
        post = Post.objects.all().filter(created__lte=max_date,created__gte=min_date).get(slug=slug)
        return render_to_response("article.html", dict(post=post))
    except ObjectDoesNotExist:
        return render_to_response("404.html")
    except DoesNotExist:
        return render_to_response("404.html")

def archive_view(request):
    tags = Post.tags.all()
    return render_to_response("archive.html", dict(tags=tags,posts=posts)

def tag_view(request):
    posts = Post.objects.all().order_by('-created').filter(tags__name=tag)
    tags = Post.tags.all()
    return render_to_response("archive_by_tag.html", dict(tags=tags,posts=posts)

#def tagpage(request, tag):
#    posts = Post.objects.all().order_by('-created').filter(tags__name=tag)
#    tags = Post.tags.all()
#    archives = Post.objects.all().order_by('-created')
#    paginator = Paginator(posts, 4)
#    try:
#        page = int(request.GET.get("page", "1"))
#    except ValueError: page = 1
#    try:
#        posts = paginator.page(page)
#    except (InvalidPage, EmptyPage):
#        posts = paginator.page(paginator.num_pages)
#    except PageNotAnInteger:
#        posts = paginator.page(1)
#    return render_to_response("tagpage.html", dict(posts=posts, user=request.user, tag=tag, tags=tags, archives=archives))

#def archives(request):
#    posts = Post.objects.all()
#    return render_to_response("archives.html", {"posts":posts})

#def bloglist(request):
#    entries = Post.objects.all().order_by('-created')
#    archives = Post.objects.all().order_by('-created')
#    tags = Post.tags.all()
#    paginator = Paginator(entries, 4)
#    try:
#        page = int(request.GET.get("page", "1"))
#    except ValueError: page = 1
#    try:
#        entries = paginator.page(page)
#    except (InvalidPage, EmptyPage):
#        entries = paginator.page(paginator.num_pages)
#    except PageNotAnInteger:
#        entries = paginator.page(1)
#    return render_to_response("blog.html", dict(entries=entries, user=request.user, archives=archives, tags=tags))
#
#def ajaxtag(request, tag):
#    entries = Post.objects.all().order_by('-created').filter(tags__name=tag)
#    paginator = Paginator(entries, 4)
#    try:
#        page = int(request.GET.get("page", "1"))
#    except ValueError: page = 1
#    try:
#        entries = paginator.page(page)
#    except (InvalidPage, EmptyPage):
#        entries = paginator.page(paginator.num_pages)
#    except PageNotAnInteger:
#        entries = paginator.page(1)
#    return render_to_response("tagpage_ajax.html", dict(entries=entries, user=request.user, tag=tag))
#
#def ajax(request):
#    entries = Post.objects.all().order_by('-created')
#    paginator = Paginator(entries, 4)
#    try:
#        page = int(request.GET.get("page", "1"))
#    except ValueError: page = 1
#    try:
#        entries = paginator.page(page)
#    except (InvalidPage, EmptyPage):
#        entries = paginator.page(paginator.num_pages)
#    except PageNotAnInteger:
#        entries = paginator.page(1)
#    return render_to_response("blog_ajax.html", dict(entries=entries, user=request.user))
#
#def pkview(request, pk):
#    archives = Post.objects.all().order_by('-created')
#    tags = Post.tags.all()
#    try: 
#        post = Post.objects.get(pk=pk)
#        return render_to_response("post.html", dict(post=post, archives=archives, tags=tags)) 
#    except ObjectDoesNotExist:
#        return render_to_response("404.html")
