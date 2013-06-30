from django.shortcuts import render_to_response
from blog.models import Post
#from blog.forms import ContactForm
#from django.template import RequestContext
#from django.core.mail import send_mail

def home(request):
#    blog.views.postview() #Render the most recent post

def about(request):
    return render_to_response("about.html")

def projects(request):
    return render_to_response("projects.html")

#def home(request):
#    return render_to_response("home.html")
#def resume(request):
#    return render_to_response("resume.html")
#def portfolio(request):
#    return render_to_response("portfolio.html")
#def contact(request):
#    success = False
#    email = ''
#    text = ''
#    if request.method == "POST":
#        contact_form = ContactForm(request.POST)
#        if contact_form.is_valid():
#            success = True
#            email = contact_form.cleaned_data['email']
#            text = contact_form.cleaned_data['text']
#            send_mail("Cheddarcode.com Contact", "A message from %s says: \n%s" % (email, text), "mailer@cheddarcode.com", ['gmiller2007@gmail.com'], fail_silently=True)
#    else:
#        contact_form = ContactForm()
#    ctx = dict(contact_form=contact_form,email=email,text=text,success=success)
#    return render_to_response("contact.html", ctx, context_instance=RequestContext(request))
