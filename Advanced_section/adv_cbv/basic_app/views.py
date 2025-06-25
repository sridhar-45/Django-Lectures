from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View , TemplateView,
                                     ListView, DetailView,
                                     CreateView, UpdateView,
                                     DeleteView)
from django.http import HttpResponse
from . import models


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("CLASS BASES VIEWS ARE COOL !!")

# # template views with CBV...
class IndexView(TemplateView):
    template_name = "basic_app/index.html"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context


class SchoolListView(ListView):
    #defaultly the ListView is return context_object..
    #customized context name...for our own..

    context_object_name = "school_list" 
    model = models.School
    # template_name = "basic_app/basic_app_basic.html"
   

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School

class SchoolUpdateView(UpdateView):  
    fields = ("name", "principal")
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")