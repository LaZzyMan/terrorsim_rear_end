from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import TerrorismData, Country, Attack, Weapon, Region, Target

class TDInfoSerialier(serializers.ModelSerializer):
    class Meta:
        model = TerrorismData
        fields = ('id', 'year', 'month', 'day', 'date', 'city',
        'summary', 'suicide', 'group_name', 'motive', 'num_kill',
        'num_wound', 'prop_value', 'prop_comment', 'country_id',
        'region_id', 'attack_type', 'target_type', 'weapon_type')

class TDGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerrorismData
        geo_field = 'location'
        fields = ('year', 'month', 'day')
        

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('country_id', 'country_name')

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
