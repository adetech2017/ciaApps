from django.contrib import admin
from .models import Voucher, MinistryOrAgency
from import_export.admin import ExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin




class MinistryOrAgencyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('mda','slug',)
    search_fields = ('mda',)

admin.site.register(MinistryOrAgency, MinistryOrAgencyAdmin)

class VoucherAdmin(admin.ModelAdmin):

    list_display = ("ministry_or_agency", "voucher_number", "date_on_voucher", "date_of_voucher_approval", "approved_by",)
    search_fields = ("mda__ministry_or_agency", "voucher_number", 'date_on_voucher', 'approved_by',)


admin.site.register(Voucher, VoucherAdmin)