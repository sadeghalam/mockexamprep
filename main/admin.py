from django.contrib import admin
from .models import UserRegistration, ContactMessage

admin.site.register(UserRegistration)
admin.site.register(ContactMessage)