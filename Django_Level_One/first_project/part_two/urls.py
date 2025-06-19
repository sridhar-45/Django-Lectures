from django.urls import path, include
from part_two.views import users, index, user_view

urlpatterns = [
    path("index/", index, name = "index"),
    path("", user_view, name = "users") 
]
