from django.contrib import admin

# Register your models here.

from .models import Mail

#admin.site.register(Mail)

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'message')  # Customize the display fields as needed
    search_fields = ('name', 'email')
    

