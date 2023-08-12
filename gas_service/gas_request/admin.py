from django.contrib import admin
from .models import GasServiceRequest

# Register your models here.

class GasServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer_name', 'contact_number', 'address', 'request_type', 'description',
                    'is_completed', 'timestamp', 'completion_timestamp')

admin.site.register(GasServiceRequest, GasServiceRequestAdmin)