from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from medtour.tours.models import (
    Tour, TourLocation, TourPaidServices, TourShots, TourAdditionalTitle,
    AdditionalInfoServices, AdditionalTitles, TourPhones, TourBookingWeekDays, CommentTour, TourMedicalProfile,
    TourBookingHoliday, TourBookingExtraHolidays
)


class LocationInline(admin.TabularInline):
    model = TourLocation


class TourShotsInline(admin.TabularInline):
    model = TourShots
    extra = 0
    readonly_fields = ["thumbnail_preview"]
    fields = ["thumbnail_preview", "photo"]

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class PaidServicesInline(admin.TabularInline):
    model = TourPaidServices
    extra = 1


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["title", "org", "category", "is_moderated", "numbers_count"]
    list_select_related = ["org", "location", "category"]
    list_editable = ["is_moderated"]
    search_fields = ["title", "org__org_name__iexact"]
    list_filter = [("org", admin.RelatedOnlyFieldListFilter)]

    ordering = ["title"]
    inlines = [
        LocationInline,
        PaidServicesInline,
        TourShotsInline,
    ]
    raw_id_fields = ["org", "category", "country", "region", "medical_profiles"]

    def numbers_count(self, obj):
        return obj.numbers.count()

    numbers_count.short_description = 'Кол. номеров'
    numbers_count.allow_tags = True


class AdditionalInfoServicesInline(admin.TabularInline):
    model = AdditionalInfoServices
    extra = 1


@admin.register(TourLocation)
class TourLocationAdmin(admin.ModelAdmin):
    raw_id_fields = ["tour"]


@admin.register(TourPaidServices)
class TourPaidServicesAdmin(admin.ModelAdmin):
    raw_id_fields = ["tour"]
    list_display = ["name", "tour"]
    list_filter = (
        ('tour', admin.RelatedOnlyFieldListFilter),
    )


@admin.register(TourShots)
class TourShotsAdmin(OrderedModelAdmin):
    """Tour Shots Admin"""
    raw_id_fields = ["tour"]
    list_display = (
        'tour',
        'move_up_down_links',
        "thumbnail_preview"
    )
    list_select_related = ["tour"]
    list_filter = [("tour", admin.RelatedOnlyFieldListFilter)]
    search_fields = ["tour__title"]

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


@admin.register(TourAdditionalTitle)
class AdditionalInfoTitleAdmin(admin.ModelAdmin):
    list_display = ["title", "tour"]
    list_filter = [("tour", admin.RelatedOnlyFieldListFilter)]
    inlines = [AdditionalInfoServicesInline]
    raw_id_fields = ["tour", "title"]


@admin.register(AdditionalInfoServices)
class AdditionalInfoServicesAdmin(admin.ModelAdmin):
    raw_id_fields = ["title"]
    list_filter = [("title__tour", admin.RelatedOnlyFieldListFilter)]
    list_display = ["title", "service", "tour_display"]
    list_select_related = ["title__tour", "title__title"]

    def tour_display(self, obj):
        return obj.title.tour

    tour_display.allow_tags = True
    tour_display.short_description = 'Тур'


@admin.register(AdditionalTitles)
class AdditionalTitlesAdmin(admin.ModelAdmin):
    list_display = ["name", "tour"]
    raw_id_fields = ["tour"]
    list_filter = [('tour', admin.RelatedOnlyFieldListFilter)]


@admin.register(TourPhones)
class TourPhonesAdmin(admin.ModelAdmin):
    raw_id_fields = ["tour"]


@admin.register(TourBookingWeekDays)
class TourBookingWeekDaysAdmin(admin.ModelAdmin):
    raw_id_fields = ["tour"]
    list_display = ["tour", "days"]
    search_fields = ["tour__title"]


@admin.register(CommentTour)
class CommentTourAdmin(admin.ModelAdmin):
    list_display = ["user", "tour", "created_at"]
    search_fields = ["tour__title"]


@admin.register(TourMedicalProfile)
class TourMedicalProfileAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(TourBookingHoliday)
class TourBookingHolidayAdmin(admin.ModelAdmin):
    list_display = ["tour", "days"]


@admin.register(TourBookingExtraHolidays)
class TourBookingExtraHolidaysAdmin(admin.ModelAdmin):
    list_display = ["tour", "date"]
    list_select_related = ["tour"]
    raw_id_fields = ["tour"]
