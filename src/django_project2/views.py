from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    mytitle = "Hello there..."
    qs = BlogPost.objects.all()[:4]
    context = {"title": "my title"}
    if request.user.is_authenticated:
        context = {"title":"Welcome to my website", "blog_list": qs}
    return render(request, 'home.html',context)

def about_page(request):
    return render(request, 'about.html',{"title":"about us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title":"contact us", 
        "form":form
    }
    return render(request, 'form.html',context)

def services_page(request):
    return render(request, 'hello_world.html',{"title":"services"})