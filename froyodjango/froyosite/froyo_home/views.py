from django.shortcuts import render
from .models import HomeEdit


# Create your views here.

def homepage(request):
    edits = HomeEdit.objects.all()
    context = {
        'edits': edits
    }
    return render(request, 'froyo_home/index.html', context)
