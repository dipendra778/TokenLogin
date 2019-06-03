from django.contrib import admin
from .models import NestedModel,LoginModel
# Register your models here.
admin.site.register(NestedModel)
admin.site.register(LoginModel)