from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import KansultatsiyaForms
from blog.models import Malumot,Yonalish,Kids,Student,Carusel


# Create your views here.
def index(request):
    yonalish = Yonalish.objects.all()
    malumots = Malumot.objects.all()
    kids = Kids.objects.all()
    student = Student.objects.all()
    carusel = Carusel.objects.all()
    kansultatsiya = KansultatsiyaForms(request.POST or None)
    if request.method == "POST" and kansultatsiya.is_valid():
        kansultatsiya.save()
        return HttpResponse("<h2> Malumotlaringiz olindi iltimos hodimimiz siz bilzn bog'lanishini kuting ! <h2/> ")
    context = {
       "malumots":malumots,
       "kansultatsiya":kansultatsiya,
        "yonalish":yonalish,
        "kids":kids,
        "student":student,
        "carusel":carusel
    }
    return render(request,"index.html",context=context)


def about(request):
    return render(request,"about.html",context={})










