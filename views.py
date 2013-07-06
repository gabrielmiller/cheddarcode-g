import datetime
from datetime import datetime
from django.shortcuts import render_to_response
from blog.models import Post

today = datetime.today().year

def about(request):
    page = "about"
    return render_to_response("about.html", dict(page="about", year=today))

def projects(request):
    return render_to_response("projects.html", dict(page="projects", year=today))

def error404(request):
    return render_to_response("404.html", dict(resource="page", year=today))
