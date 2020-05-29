from django.contrib import admin
from .models import Enquiries
from django.core.mail import send_mail
# Register your models here.

def sendMail():
    sendMail.short_description = "Send new year greetings"
    objects = Enquiries.objects.all()

    for obj in objects:
        message = f"Hi {obj.name}, \n\t\t Wish you a Happy New Year!\n\nRegards,\nClean Photography"
        send_mail("Greetings from Clean Photography",message,"zeva.connect@gmail.com",[obj.email,])


class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    actions = [sendMail]


admin.site.register(Enquiries,EnquiriesAdmin)