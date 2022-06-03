from django.contrib import admin
from .models import Address, Contact, MessageBox

# Register your models here.

admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(MessageBox)
