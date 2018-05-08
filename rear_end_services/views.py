from rest_framework import permissions, renderers, status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rear_end_services import serializers, models
from rest_framework import filters
# Create your views here.


class YearFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        year = request.query_params.get('year', None)
        if year is not None:
            return queryset.filter(year=year)
        else:
            return queryset


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer


class AttackViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Attack.objects.all()
    serializer_class = serializers.AttackSerializer


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer


class TargetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Target.objects.all()
    serializer_class = serializers.TargetSerializer


class TDInfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TerrorismData.objects.all()
    serializer_class = serializers.TDInfoSerialier

class TDGeneralViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TerrorismData.objects.all()
    serializer_class = serializers.TDGeoSerializer
    filter_backends = (YearFilter,)
