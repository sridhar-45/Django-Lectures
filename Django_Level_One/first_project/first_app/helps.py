from django.shortcuts import render

#this duplicate of views.py for ..practice purpose...
def helps(request):
    return render(request, "first_app/help.html")