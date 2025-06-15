from django.shortcuts import render
from django.http import HttpResponse
from part_two.models import Users
from part_two.forms import user_form

# Create your views here.
def index(request):
    return render(request, 'part_two/index.html')


def users(request):
    user_list = Users.objects.order_by('first_name')
    user_dict = {'users' : user_list}
    return render(request, 'part_two/users.html', context = user_dict)


def user_view(request):
    user_list = Users.objects.order_by('first_name')
    form = user_form()
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            form.save(commit = True ) # saves data to database
            # return render(request, 'part_two/users.html', {'users' : form})
            return index(request) # returns to index.html
        
    
    
    return render(request, 'part_two/user_form.html', {'form' : form})    
    