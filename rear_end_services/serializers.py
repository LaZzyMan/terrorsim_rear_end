from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import TerrorismData, Country, Attack, Weapon, Region, Target, Keyword
        

class CountryGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Country
        geo_field = 'boundary'
        fields = ('country_id', 'country_name', 'region_id')


class RegionGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Region
        geo_field = 'boundary'
        fields = ('region_id', 'region_name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_id', 'country_name', 'region_id')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('region_id', 'region_name')


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = ('attack_type_id', 'attack_type_name')


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ('target_type_id', 'target_type_name')


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ('weapon_type_id', 'weapon_type_name')


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('word_id', 'word', 'frequency')


class TDInfoSerialier(GeoFeatureModelSerializer):
    country = CountrySerializer()
    region = RegionSerializer()
    attack_type = AttackSerializer()
    weapon_type = WeaponSerializer()
    target_type = TargetSerializer()
    keywords = KeywordSerializer()
    class Meta:
        model = TerrorismData
        geo_field = 'location'
        fields = ('id', 'year', 'month', 'day', 'date', 'city',
        'summary', 'suicide', 'group_name', 'motive', 'num_kill',
        'num_wound', 'prop_value', 'prop_comment', 'country',
        'region', 'attack_type', 'target_type', 'weapon_type', 'keywords')


class TDGeoSerializer(GeoFeatureModelSerializer):
    country = CountrySerializer()
    day_in_year = serializers.SerializerMethodField()

    class Meta:
        model = TerrorismData
        geo_field = 'location'
        fields = ('id', 'year', 'month', 'day', 'city', 'country', 'day_in_year')
    
    def get_day_in_year(self, obj):
        return obj.date.timetuple().tm_yday

