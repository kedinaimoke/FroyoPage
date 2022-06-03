from django.shortcuts import render
from .models import Group, Flavour


# Create your views here.

def product(request):
    groups = Group.objects.all()
    flavours = Flavour.objects.all()
    context = {
        'groups': groups,
        'flavours': flavours
    }
    return render(request, 'froyo_product/product.html', context)
