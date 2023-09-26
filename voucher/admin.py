from django.contrib import admin
from .models import Voucher, MinistryOrAgency





class MinistryOrAgencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(MinistryOrAgency, MinistryOrAgencyAdmin)

class VoucherAdmin(admin.ModelAdmin):

    list_display = ("ministry_or_agency", "voucher_number", "date_on_voucher", "date_of_voucher_approval", "approved_by",)
    search_fields = ("name__ministry_or_agency", "voucher_number", 'date_on_voucher', 'approved_by',)


admin.site.register(Voucher, VoucherAdmin)