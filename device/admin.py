from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import device

#admin.site.register(device)

@admin.register(device)
class DeviceImportExport(ImportExportModelAdmin):
    pass