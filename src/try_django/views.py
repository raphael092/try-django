from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h1>#bethebestyou</h1>")

def about_page(request):
    return HttpResponse("<h1>about us")
    
def contact_page(request):
    return HttpResponse("<h1>contact us!</h1>")
     