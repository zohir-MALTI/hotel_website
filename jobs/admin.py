from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job


class JobAdmin(ImportExportModelAdmin):
    class Meta:
        model = Job

admin.site.register(Job, JobAdmin)
