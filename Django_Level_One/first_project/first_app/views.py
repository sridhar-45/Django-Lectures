from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, WebPage 

# Create your views here.
def home(request):
    webpage_list = AccessRecord.objects.order_by('date')
    # mydict = {"insert_me" : "hello programmer welcome to django !!!!"}
    date_dict = {"access_records" : webpage_list }
    return render(request, "first_app/index.html", context = date_dict)
