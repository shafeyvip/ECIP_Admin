from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Profile

#admin.site.register(Profile)

@admin.register(Profile)
class ProfileImportExport(ImportExportModelAdmin):
    pass