from django.contrib import admin

from medtour.applications.models import Application, TourApplication


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["fullName", "created_at"]


@admin.register(TourApplication)
class TourApplicationAdmin(admin.ModelAdmin):
    list_display = ["tour", "status"]
    list_select_related = ["application__category", "tour"]
