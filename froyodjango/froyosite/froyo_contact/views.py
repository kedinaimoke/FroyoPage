from django.shortcuts import render
from .forms import ContactForm
from .models import Address, Contact, MessageBox


# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        email = request.POST.get('contact_mail', '')
        if Contact.objects.filter(email=email).exists():
            return render(request, 'froyo_contact/failed.html')
        elif form.is_valid():
            form.save()
            name = request.POST.get('contact_name', '')
            recipient = request.POST.get('contact_mail', '')
            receiver_detail = {
                'recipient': recipient,
                'name': name
            }
            return render(request, 'froyo_contact/success.html', receiver_detail)
    form = ContactForm()
    address = Address.objects.all()
    message = MessageBox.objects.all()
    context = {
        'form': form,
        'address': address,
        'message': message
    }
    return render(request, 'froyo_contact/contact.html', context)
