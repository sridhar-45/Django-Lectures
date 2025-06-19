from django.urls import path, include
from . import views

#TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    path("", views.index , name = "index"),
    path("register/", views.register, name = "register"),
    
]
