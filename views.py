from django.shortcuts import render_to_response
from blog.models import Post

def about(request):
    page = "about"
    return render_to_response("about.html", dict(page="about"))

def projects(request):
    return render_to_response("projects.html", dict(page="projects"))

def error404(request):
    return render_to_response("404.html", dict(resource="page"))
