from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(Page)
admin.site.register(PageOption)
admin.site.register(Stepper)
admin.site.register(CollectedData)