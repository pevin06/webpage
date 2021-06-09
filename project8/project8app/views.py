from django.shortcuts import render
from . models import Place
from . models import New
# Create your views here.
def demo(request):
    obj = Place.objects.all()
    sub = New.objects.all()
    return render(request,"index.html",{'result':obj,'any':sub})

