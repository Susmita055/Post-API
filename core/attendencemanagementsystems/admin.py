from django.contrib import admin
from .models import User, ContactDetails

# Register your models here.
admin.site.register(User)
admin.site.register(ContactDetails)
