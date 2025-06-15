from django.urls import path
from .views import index, other, relative, base

app_name = "basic_app"
urlpatterns = [
    path("", index, name = "index"),
    path("other/", other, name = "other"),
    path("relative/", relative, name = "relative"),
    path("base/", base, name ="base")
]
