from django.shortcuts import render_to_response
from blog.models import Post

def about(request):
    return render_to_response("about.html")

def projects(request):
    return render_to_response("projects.html")

def error404(request):
    return render_to_response("404.html")
