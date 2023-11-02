from django.contrib import admin
from django.contrib import admin
from appbarberia.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=["dni", "first_name", "last_name", "phone"]
    pass

admin.site.register(Customer, CustomerAdmin)