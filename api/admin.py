from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_details']

admin.site.register(Vendor, VendorAdmin)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)