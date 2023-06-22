from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.exceptions import PermissionDenied

from medtour.applications.serializers import (ListTourApplicationSerializer,
                                              PostApplicationSerializer, UpdateTourApplicationSerializer,
                                              RetrieveTourApplicationSerializer, CommentTourApplicationSerializer)
from medtour.applications.models import TourApplication, Application, CommentTourApplication
from medtour.contrib.pagination import StandardResultsSetPagination
from medtour.contrib.serializers import ReadWriteSerializerMixin


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = PostApplicationSerializer

