from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there..."
    #doc = "<h1>{title}</h1>".format(title=title)
    #django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
    #return HttpResponse("<h1>#bethebestyou</h1>")
    return render(request, "hello_world.html", {"title": my_title})

def about_page(request):
    return render(request, "about.html", {"title": "About us"})
    
def contact_page(request):
    return render(request, "about.html", {"title": "Contact us"})
     
#def example_page(request):              #returns "hello_world.html"
    context = {"title": "Example"}
    something_here = "hello_world.html"
    return HttpResponse(something_here)

def example_page(request):              #returns an item"
    context         = {"title": "Example"}
    template_name   = "hello_world.html"
    template_obj    = get_template(template_name)
    rendered_item   = template_obj.render(context)
    return HttpResponse(rendered_item)
     