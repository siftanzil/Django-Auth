from django.shortcuts import render

# Create your views here.


# index page

def index(request):
    diction = {}
    return render(request, "Login_app/index.html", context=diction)