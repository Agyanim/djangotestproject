from django.http import HttpResponse

def aboutController():
    return HttpResponse("<p> This is my about page About page</p>")
    