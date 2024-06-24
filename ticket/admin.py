from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Ticket, IT

# Register your models here.
#admin.site.register(Ticket)
#admin.site.register(IT)

@admin.register(Ticket)
class TicketImportExport(ImportExportModelAdmin):
    pass


@admin.register(IT)
class ITImportExport(ImportExportModelAdmin):
    pass