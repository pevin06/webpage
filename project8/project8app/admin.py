from django.contrib import admin

# Register your models here.
from .models import Place
admin.site.register(Place)
from .models import New
admin.site.register(New)
