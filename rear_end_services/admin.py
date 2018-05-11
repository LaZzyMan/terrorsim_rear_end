from django.contrib.gis import admin
from .models import Country, Attack, Weapon, Target, Region, TerrorismData, Keyword

# Register your models here.

# admin.register(WorldBorder, admin.GeoModelAdmin)

admin.site.site_header = '后台数据管理'
admin.site.site_title = '数据管理平台'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['countryId', 'countryName']
    ordering = ['countryId']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['regionId', 'regionName']
    ordering = ['regionId']


@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = ['attackTypeId', 'attackTypeName']
    ordering = ['attackTypeId']


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['targetTypeId', 'targetTypeName']
    ordering = ['targetTypeId']


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['weaponTypeId', 'weaponTypeName']
    ordering = ['weaponTypeId']


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['wordId', 'word', 'frequency']
    search_fields = ['wordId']
    ordering = ['wordId']


@admin.register(TerrorismData)
class TDAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'country', 'city', 'numKill', 'numWound']
    list_per_page = 30
    list_filter = ['date', 'region', 'attackType', 'targetType', 'weaponType']
    search_fields = ['country']

