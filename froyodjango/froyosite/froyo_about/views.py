from django.shortcuts import render
from .models import Main, SideInfo


# Create your views here.

def about(request):
    sides = SideInfo.objects.all()
    mains = Main.objects.all()
    context = {
        'sides': sides,
        'mains': mains
    }
    return render(request, 'froyo_about/about.html', context)
