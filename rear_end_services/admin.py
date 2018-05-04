from django.contrib.gis import admin
from .models import WorldBorder, GlobalTerrorism, Country, Attack, Weapon, Target, Region, TerrorismData

# Register your models here.

# admin.register(WorldBorder, admin.GeoModelAdmin)

admin.site.site_header = '后台数据管理'
admin.site.site_title = '数据管理平台'


@admin.register(WorldBorder)
class WorldBorderAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(GlobalTerrorism)
class GlobalTerrorismAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'year', 'month', 'day')
    list_per_page = 50
    ordering = ('-id',)
    list_filter = ('year', 'month', 'day')
    search_fields = ('id', 'year', 'month', 'day')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    pass


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    pass


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['weapon_type_id', 'weapon_type_name']
    list_filter = ['weapon_type_id']


@admin.register(TerrorismData)
class TDAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'country_id', 'city', 'num_kill', 'num_wound']
    list_per_page = 30
    list_filter = ['date']
    search_fields = ['country_id', 'region_id', 'attack_type', 'target_type', 'weapon_type']
