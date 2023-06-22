from django.contrib import admin

from medtour.guides.models import (Guide, GuideReview,
                                   GuideShots, GuideProgram, GuideServices, GuideCategory, ProgramSchedule,
                                   ProgramPlaces, ProgramShots, ProgramReview)


class ProgramScheduleInline(admin.TabularInline):
    model = ProgramSchedule
    extra = 0


class ProgramPlacesInline(admin.TabularInline):
    model = ProgramPlaces
    extra = 0


class GuideProgramInline(admin.TabularInline):
    model = GuideProgram
    extra = 0


class ProgramShotsInline(admin.TabularInline):
    model = ProgramShots
    extra = 0


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ["title", "org"]
    inlines = [GuideProgramInline]


@admin.register(GuideReview)
class GuideReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramReview)
class ProgramReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(GuideShots)
class GuideShotsAdmin(admin.ModelAdmin):
    pass


@admin.register(GuideProgram)
class GuideProgramAdmin(admin.ModelAdmin):
    raw_id_fields = ['guide']
    list_select_related = ['guide']
    inlines = [
        ProgramShotsInline,
        ProgramScheduleInline,
        ProgramPlacesInline,
    ]


@admin.register(GuideServices)
class GuideServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(GuideCategory)
class GuideCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramSchedule)
class ProgramScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramPlaces)
class ProgramPlacesAdmin(admin.ModelAdmin):
    pass


@admin.register(ProgramShots)
class ProgramShotsAdmin(admin.ModelAdmin):
    pass
