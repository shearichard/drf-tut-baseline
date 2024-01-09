from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from places.models import Country
from places.serializers import CountrySerializer
from places.permissions import IsOwnerOrReadOnly

class CountryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]



