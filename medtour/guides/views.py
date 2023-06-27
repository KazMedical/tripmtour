from django.db import models
from django.db.models import Q, Min, Count, Avg
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from medtour.contrib.required_field_list_view.viewsets import TourIdRequiredFieldsModelViewSet
from medtour.guides.serializers import GuideProgramSerializer, GuideReviewSerializer, GuideSerializer, \
    GuideServicesSerializer, GuideShotsSerializer, GuideProgramListSerializer, GuideProgramDetailSerializer, \
    GuideListSerializer, GuideReadSerializer, GuidePOSTShotsSerializer, ProgramPlacesSerializer, \
    ProgramScheduleSerializer, ProgramReviewSerializer
from medtour.guides.models import Guide, GuideProgram, GuideReview, GuideServices, GuideShots, ProgramPlaces, \
    ProgramSchedule, ProgramReview, Round
from medtour.tours.models import Tour


class GuideViewSet(TourIdRequiredFieldsModelViewSet):
    queryset = Guide.objects.select_related("region", "country").prefetch_related("guide_shots")
    serializer_class = GuideSerializer
    retrieve_serializer_class = GuideReadSerializer
    list_serializer_class = GuideListSerializer

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return self.serializer_class
        elif self.action == "list":
            return self.list_serializer_class
        return self.retrieve_serializer_class

    @extend_schema(
        parameters=[OpenApiParameter(name="tour_id", required=True, type=int)])
    def list(self, request, *args, **kwargs):
        tour_id = request.query_params.get('tour_id')
        if not tour_id:
            return Response(
                {
                    "message": _("Обязательный параметр tour_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        tour_obj = Tour.objects.filter(pk=tour_id)
        if tour_obj.exists():
            tour_obj = tour_obj.first()
            if not tour_obj.region_id:
                return Response(
                    {
                        "message": _("Не найден подходящий тур")
                    },
                    status=status.HTTP_400_BAD_REQUEST)
            qs = self.get_queryset().filter(region_id=tour_obj.region_id)[:24].annotate(
                minimum_price=Min("programs__price", filter=Q(programs__is_deleted=False))
            ).prefetch_related("guide_shots", "programs")  # TODO: optimize guide_reviews sql queries
            serializer = self.get_serializer(qs, many=True)
            return Response(serializer.data)
        else:
            return Response(
                {
                    "message": _("Не найден подходящий тур")
                },
                status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(name="org_id", required=True, type=int),
        ])
    @action(detail=False)
    def partner(self, request, *args, **kwargs):
        org_id = self.request.query_params.get('org_id')
        if not org_id:
            return Response(
                {
                    "message": _("Обязательный параметр org_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        qs = Guide.objects.filter(org_id=org_id)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class GuideReviewViewSet(viewsets.ModelViewSet):
    queryset = GuideReview.objects.all()
    serializer_class = GuideReviewSerializer
    http_method_names = ["get", "post"]
    filterset_fields = ["guide_id"]

    @extend_schema(
        parameters=[OpenApiParameter(name="guide_id", required=True, type=int)],
        responses={"200": GuideReviewSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        guide_id = request.query_params.get('guide_id')  # noqa
        if not guide_id:
            return Response(
                {
                    "message": _("Обязательный параметр guide_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class ProgramReviewViewSet(viewsets.ModelViewSet):
    queryset = ProgramReview.objects.all()
    serializer_class = ProgramReviewSerializer
    http_method_names = ["get", "post"]
    filterset_fields = ["program_id"]

    @extend_schema(
        parameters=[OpenApiParameter(name="program_id", required=True, type=int)],
        responses={"200": ProgramReviewSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        program_id = request.query_params.get('program_id')  # noqa
        if not program_id:
            return Response(
                {
                    "message": _("Обязательный параметр program_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class GuideShotsViewSet(viewsets.ModelViewSet):
    queryset = GuideShots.objects.all()
    serializer_class = GuideShotsSerializer
    post_serializer_class = GuidePOSTShotsSerializer
    filterset_fields = ["guide_id"]

    def get_serializer_class(self):
        if self.action == "create":
            return self.post_serializer_class
        return self.serializer_class

    @extend_schema(
        parameters=[OpenApiParameter(name="guide_id", required=True, type=int)],
        responses={"200": GuideShotsSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        guide_id = request.query_params.get('guide_id')  # noqa
        if not guide_id:
            return Response(
                {
                    "message": _("Обязательный параметр guide_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class GuideProgramViewSet(viewsets.ModelViewSet):
    queryset = GuideProgram.objects.prefetch_related(
        "services", "excluded_services", "program_shots").select_related("guide")
    serializer_class = GuideProgramSerializer
    filterset_fields = ["guide_id", "category_id"]
    list_serializer_class = GuideProgramListSerializer
    retrieve_serializer_class = GuideProgramDetailSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == "list":
            return qs.filter(
                guide__is_deleted=False, guide__is_moderated=True
            ).annotate(
                service__avg=Round(Avg('program_reviews__service'), 2, output_field=models.FloatField()),
                location__avg=Round(Avg('program_reviews__location'), 2, output_field=models.FloatField()),
                staff__avg=Round(Avg('program_reviews__staff'), 2, output_field=models.FloatField()),
                proportion__avg=Round(Avg('program_reviews__proportion'), 2, output_field=models.FloatField()),
                comments__count=Count('program_reviews__service', output_field=models.IntegerField())
            )
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.list_serializer_class(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        responses={"200": GuideProgramDetailSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.retrieve_serializer_class(instance)
        return Response(serializer.data)


class GuideServicesViewset(viewsets.ModelViewSet):
    queryset = GuideServices.objects.all()
    serializer_class = GuideServicesSerializer
    filterset_fields = ["guide_id"]

    @extend_schema(
        parameters=[OpenApiParameter(name="guide_id", required=True, type=int)],
        responses={"200": GuideServicesSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        guide_id = request.query_params.get('guide_id')  # noqa
        if not guide_id:
            return Response(
                {
                    "message": _("Обязательный параметр guide_id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)


class GuideManyViewWithoutPagination(generics.ListAPIView):
    queryset = Guide.objects.annotate(
        minimum_price=Min("programs__price", filter=Q(programs__is_deleted=False))
    ).prefetch_related('programs', 'guide_shots')
    serializer_class = GuideListSerializer

    @extend_schema(summary="Получение много гидов по конкретным id",
                   parameters=[OpenApiParameter(name="id__in", description="Введите id__in гидов", required=True)],
                   responses={'200': GuideListSerializer(many=True)},
                   )
    @action(detail=False)
    def get(self, request, *args, **kwargs):  # noqa
        ids = request.query_params.get('id__in')  # noqa
        if not ids:
            return Response({"message": _("Обязательный параметр id__in не указан.")},
                            status=status.HTTP_400_BAD_REQUEST)
        qs = self.get_queryset().filter(id__in=ids.split(','))
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class GuideProgramManyViewWithoutPagination(generics.ListAPIView):
    queryset = GuideProgram.objects.all()
    serializer_class = GuideListSerializer

    @extend_schema(summary="Получение много програм гидов по конкретным id",
                   parameters=[
                       OpenApiParameter(name="id__in", description="Введите id__in програм гидов", required=True)],
                   responses={'200': GuideProgramListSerializer(many=True)},
                   )
    @action(detail=False)
    def get(self, request, *args, **kwargs):  # noqa
        ids = request.query_params.get('id__in')  # noqa
        if not ids:
            return Response({"message": _("Обязательный параметр id__in не указан.")},
                            status=status.HTTP_400_BAD_REQUEST)
        qs = self.get_queryset().filter(id__in=ids.split(','))
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)


class GuideSlugView(generics.RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideReadSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_object(self):
        try:
            obj = self.queryset.get(slug=self.kwargs.get(self.lookup_url_kwarg))
        except Guide.DoesNotExist:
            raise Http404
        return obj


class ProgramPlacesAPIView(viewsets.ModelViewSet):
    queryset = ProgramPlaces.objects.all()
    serializer_class = ProgramPlacesSerializer
    filterset_fields = ["program_id"]


class ProgramScheduleAPIView(viewsets.ModelViewSet):
    queryset = ProgramSchedule.objects.all()
    serializer_class = ProgramScheduleSerializer
    filterset_fields = ["program_id"]
