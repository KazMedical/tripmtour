from django.utils.translation import gettext_lazy as _
from drf_spectacular import types
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from ordered_model.serializers import OrderedModelSerializer
from rest_framework import serializers
from rest_framework.filters import OrderingFilter

from medtour.contrib.sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField
from medtour.guides.models import Guide, GuideProgram, GuideReview, GuideServices, GuideShots, ProgramSchedule, \
    ProgramPlaces, ProgramShots, ProgramReview
from medtour.tours.models import TourShots
from medtour.users.serializers import CountrySerializer, RegionSerializer
from medtour.utils.constants import LanguagesChoice


class GuideServicesSmallSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class GuideReviewSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source="user.avatar", read_only=True, allow_null=True, required=False)
    userData = serializers.SerializerMethodField(read_only=True, allow_null=True)

    class Meta:
        model = GuideReview
        fields = "__all__"

    @extend_schema_field(types.OpenApiTypes.STR)
    def get_userData(self, instance):
        if hasattr(instance.user, "people"):
            return instance.user.people.first_name + " " + instance.user.people.last_name
        elif hasattr(instance.user, "organization"):
            return instance.user.organization.org_name
        return _("Удалённый аккаунт")


class ProgramReviewSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source="user.avatar", read_only=True, allow_null=True, required=False)  # noqa
    userData = serializers.SerializerMethodField(read_only=True, allow_null=True)

    class Meta:
        model = ProgramReview
        fields = "__all__"

    @extend_schema_field(types.OpenApiTypes.STR)
    def get_userData(self, instance):
        if hasattr(instance.user, "people"):
            return instance.user.people.first_name + " " + instance.user.people.last_name
        elif hasattr(instance.user, "organization"):
            return instance.user.organization.org_name
        return _("Удалённый аккаунт")


class AverageGuideRatingSerializer(serializers.Serializer):
    service__avg = serializers.FloatField(allow_null=True)
    location__avg = serializers.FloatField(allow_null=True)
    staff__avg = serializers.FloatField(allow_null=True)
    proportion__avg = serializers.FloatField(allow_null=True)
    reviews__count = serializers.IntegerField(allow_null=True)


class GuidePOSTShotsSerializer(OrderedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = GuideShots
        exclude = ("order",)


class GuideShotsSerializer(OrderedModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = GuideShots
        fields = "__all__"


class GuideSerializer(serializers.ModelSerializer):
    guide_shots = GuideShotsSerializer(read_only=True, many=True, required=False, allow_null=True)
    minimum_price = serializers.IntegerField(read_only=True, default=0)
    is_moderated = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = Guide
        exclude = ("created_at", "is_deleted", "is_subscribed", "is_top")


class GuideReadSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=False, read_only=True)
    country = CountrySerializer(many=False, read_only=True)
    average_rating = serializers.SerializerMethodField()
    guide_shots = GuideShotsSerializer(read_only=True, many=True, required=False, allow_null=True)

    class Meta:
        model = Guide
        fields = "__all__"

    @extend_schema_field(AverageGuideRatingSerializer)
    def get_average_rating(self, instance):
        return instance.average_rating


class GuideListSerializer(serializers.ModelSerializer):
    guide_shots = GuideShotsSerializer(read_only=True, many=True, required=False, allow_null=True)
    minimum_price = serializers.IntegerField(read_only=True, default=0)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Guide
        fields = ("id", "title", "guide_shots", "minimum_price", "average_rating")

    @extend_schema_field(AverageGuideRatingSerializer)
    def get_average_rating(self, instance):
        return instance.average_rating


class ProgramScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramSchedule
        fields = "__all__"


class ProgramPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramPlaces
        fields = "__all__"


class GuideProgramSerializer(serializers.ModelSerializer):
    languages = serializers.MultipleChoiceField(choices=LanguagesChoice.choices)

    class Meta:
        model = GuideProgram
        fields = "__all__"


class ProgramShotsSerializer(serializers.ModelSerializer):
    thumbnail = HyperlinkedSorlImageField(
        '570x360',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = ProgramShots
        fields = ("thumbnail",)


class GuideProgramListSerializer(serializers.ModelSerializer):
    program_shots = ProgramShotsSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField(allow_null=True, default=3.5)
    city = serializers.StringRelatedField(source="guide.city.name", allow_null=True)
    reviews_count = serializers.SerializerMethodField(read_only=True)
    is_top = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = GuideProgram
        fields = ["id", "title", "program_shots", "price",
                  "seats_count", "avg_rating", "city", "reviews_count", "is_top"]

    @extend_schema_field(OpenApiTypes.NUMBER)
    def get_avg_rating(self, obj):
        rating_dict = {
            'service': obj.service__avg,
            'location': obj.location__avg,
            'staff': obj.staff__avg,
            'proportion': obj.proportion__avg,
        }
        values = [value for value in rating_dict.values() if value is not None]
        average = round(sum(values) / len(values), 1) if values else None
        return average

    @extend_schema_field(OpenApiTypes.INT)
    def get_reviews_count(self, obj):
        return obj.comments__count

    @extend_schema_field(OpenApiTypes.BOOL)
    def get_is_top(self, obj):
        return obj.guide.is_top


class GuideProgramDetailSerializer(serializers.ModelSerializer):
    languages = serializers.MultipleChoiceField(choices=LanguagesChoice.choices)
    program_shots = ProgramShotsSerializer(many=True)
    services = GuideServicesSmallSerializer(read_only=True, many=True)
    excluded_services = GuideServicesSmallSerializer(read_only=True, many=True)
    guide_name = serializers.StringRelatedField(source='guide.title')
    average_rating = serializers.SerializerMethodField()
    schedules = serializers.SerializerMethodField()
    places = ProgramPlacesSerializer(many=True, label="Местности программы")

    class Meta:
        model = GuideProgram
        fields = "__all__"

    @extend_schema_field(ProgramScheduleSerializer(many=True, label="Расписание программы гида"))
    def get_schedules(self, obj):
        schedules = obj.schedules.all().order_by('start_time')
        serializer = ProgramScheduleSerializer(schedules, many=True)
        return serializer.data

    @extend_schema_field(AverageGuideRatingSerializer)
    def get_average_rating(self, instance):
        return instance.guide.average_rating


class GuideServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideServices
        fields = "__all__"
