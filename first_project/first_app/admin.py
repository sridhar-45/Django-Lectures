from django.contrib import admin
from first_app.models import AccessRecord, Topic, WebPage
from part_two.models  import Users

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(Users)