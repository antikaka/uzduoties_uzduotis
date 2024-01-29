from django.contrib import admin
from .models import Uzduotis

# Register your models here.
class Uzduotisadmin(admin.ModelAdmin):
    list_display = ("data", "vartotojas")
    list_filter = ("data", "vartotojas")


admin.site.register(Uzduotis)

