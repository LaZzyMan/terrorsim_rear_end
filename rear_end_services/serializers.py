from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import TerrorismData


class TDSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerrorismData
        geo_field = 'location'
        id_field = False
        auto_field = True
        fields = ('id', 'location', 'date', 'country_id', 'region_id')
