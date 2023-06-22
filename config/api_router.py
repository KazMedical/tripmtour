from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


# TOURS
from medtour.tours.views import TourViewSet

# GUIDES
from medtour.guides.views import GuideViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# USERS
# router.register("users", UserViewSet)
# router.register("partners", OrganizationViewSet)
# router.register("clients", PersonViewSet)
# router.register("address/country", CountryView)
# router.register("address/regions", RegionView)
# router.register("address/cities", CityView)
# TODO: Remove this line
# router.register("address/first-page", MainPageCountryView)
# router.register("phone", PhoneNumberView)
# router.register("email", EmailAddressView)

# TOURS
router.register("tours", TourViewSet, basename="tours")
# router.register("packages", TourPackagesView)
# router.register("paid-services", TourPaidServicesView)
# router.register("location", TourLocationView)
# router.register("shots", TourShotsView, basename='tour-shots')
# router.register("additionalInfo/title", AdditionalTitleViewset)
# router.register("additionalInfo/tourTitle", AdditionalInfoTitleViewSet)
# router.register("additionalInfo/Services", AdditionalInfoServicesViewSet)
# router.register("comments", TourCommentView)
# router.register("numbers", TourNumbersView, basename='tour-numbers')
# router.register("number-shots", NumberShotsViewSet, basename='number-shots-get')
# router.register("org_type", OrgCategoryView)
# router.register("tourPrice", TourPriceFileView)
# router.register("tour-apps/apps", TourApplicationViewSet)
# router.register("tour-apps/comments", CommentTourApplicationViewSet)
# router.register("entry-days", TourBookingWeekDaysViewSet)
# router.register("holidays", TourBookingHolidayViewSet)
# router.register("extra-holiday", TourBookingExtraHolidaysViewSet)
# router.register("phones", TourPhonesView)

# router.register("number-cabinets", NumberCabinetsView)

# GUIDES
router.register('guides', GuideViewSet)
# router.register('guide-reviews', GuideReviewViewSet)
# router.register('program-reviews', ProgramReviewViewSet)
# router.register('guide-shots', GuideShotsViewSet)
# router.register('guide-programs', GuideProgramViewSet)
# router.register('guide-services', GuideServicesViewset)
# router.register('guide-program-places', ProgramPlacesAPIView)
# router.register('guide-program-schedules', ProgramScheduleAPIView)

app_name = "v1"
urlpatterns = router.urls

urlpatterns += [
    # path("users/", include("medtour.users.urls", namespace="users-api")),
    path('applications/', include("medtour.applications.urls", namespace="applications")),

    # path('tours/slug/<slug:slug>/', TourSlugView.as_view(), name='tours-detail-slug'),
    # path('guides/slug/<slug:slug>/', GuideSlugView.as_view(), name='guides-detail-slug'),
    # path('numbers/comforts/', NumberComfortView.as_view(), name='tour-number-comforts'),
    # path('manyTours/', TourManyViewWithoutPagination.as_view(), name='many-tours-list'),
    # path('manyGuides/', GuideManyViewWithoutPagination.as_view(), name='many-guides-list'),
    # path('manyGuidePrograms/', GuideProgramManyViewWithoutPagination.as_view(), name='many-guide-programs-list'),

    path("", include("medtour.main.urls", namespace="contents")),
]
