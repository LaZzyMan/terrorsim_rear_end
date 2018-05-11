from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import TerrorismData, Country, Attack, Weapon, Region, Target, Keyword
        

class CountryGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Country
        geo_field = 'boundary'
        fields = ('countryId', 'countryName', 'region')


class RegionGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Region
        geo_field = 'boundary'
        fields = ('regionId', 'regionName')


class CountrySerializer(serializers.ModelSerializer):
    # sumKill = serializers.SerializerMethodField()
    # sumWound = serializers.SerializerMethodField()
    # sumProp = serializers.SerializerMethodField()
    class Meta:
        model = Country
        fields = ('countryId', 'countryName', 'region')



class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('regionId', 'regionName')


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ('attackTypeId', 'attackTypeName')


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('targetTypeId', 'targetTypeName')


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('weaponTypeId', 'weaponTypeName')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('wordId', 'word', 'frequency')


class TDInfoSerialier(GeoFeatureModelSerializer):
    country = CountrySerializer()
    region = RegionSerializer()
    attackType = AttackSerializer()
    weaponType = WeaponSerializer()
    targetType = TargetSerializer()
    # keywords = KeywordSerializer(many=True)
    class Meta:
        model = TerrorismData
        geo_field = 'location'
        fields = ('id', 'year', 'month', 'day', 'date', 'city',
        'summary', 'suicide', 'groupName', 'motive', 'numKill',
        'numWound', 'propValue', 'propComment', 'country',
        'region', 'attackType', 'targetType', 'weaponType',)
        


class TDGeoSerializer(GeoFeatureModelSerializer):
    country = CountrySerializer()
    dayInYear = serializers.SerializerMethodField()

    class Meta:
        model = TerrorismData
        geo_field = 'location'
        fields = ('id', 'year', 'month', 'day', 'city', 'country', 'dayInYear')
    
    def get_dayInYear(self, obj):
        return obj.date.timetuple().tm_yday

