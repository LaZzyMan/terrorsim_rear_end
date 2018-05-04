from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import WorldBorder, GlobalTerrorism, TerrorismData


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = 'mpoly'
        auto_field = True
        id_field = False
        fields = ('name', 'area', 'pop2005')


class GlobalTerrorismSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = GlobalTerrorism
        geo_field = 'geom'
        id_field = False
        auto_field = True
        fields = ('year', 'month', 'day')

