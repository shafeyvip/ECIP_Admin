from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import employee

#admin.site.register(employee)

@admin.register(employee)
class EmployeeImportExport(ImportExportModelAdmin):
    pass