from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Student, Document, Reason

# Register your models here.


class DocumentInline(admin.StackedInline):
    model = Document
    extra = 1


class ReasonInline(admin.StackedInline):
    model = Reason
    extra = 1


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [DocumentInline, ReasonInline]
    list_display = (
        "id",
        "name",
        "passport_number",
        "nationality",
        "department",
        "status",
    )
    search_fields = (
        "first_name",
        "last_name",
        "student_id",
        "passport_number",
    )
    list_display_links = ("name",)
