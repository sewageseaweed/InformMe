from django.shortcuts import render

# Create your views here.
def inform_me(request):
    return render(request, "home.html", {})
   