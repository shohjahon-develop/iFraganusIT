from django.contrib import admin

from blog.models import Malumot,Kansultatsiya,Yonalish,Kids,Student,Carusel

# Register your models here.
admin.site.register(Yonalish)
admin.site.register(Kids)
admin.site.register(Student)
admin.site.register(Carusel)
@admin.register(Kansultatsiya)
class KansultatsiyaAdmin(admin.ModelAdmin):
    list_display = ['name','phonenumber']
    list_filter = ['name',"phonenumber"]
    prepopulated_fields = {"name": ('phonenumber',)}


@admin.register(Malumot)
class MalumotAdmin(admin.ModelAdmin):
    list_display = ['name','bio']
    list_filter = ['name',"bio"]
    prepopulated_fields = {"name": ('bio',)}

























