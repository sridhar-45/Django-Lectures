from django.urls import path, include
from . import views, helps

urlpatterns = [
    path("", views.home, name = "home"),
    path("helps/", helps.helps, name = 'help'),
]
