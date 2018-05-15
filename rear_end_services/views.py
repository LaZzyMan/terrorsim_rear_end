from rest_framework import permissions, renderers, status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from rear_end_services import serializers, models
from rest_framework import filters
from datetime import datetime
from django.db.models import Sum, Count, F
from django.contrib.gis.geos import Polygon, GEOSGeometry
import json
from rest_framework_swagger.views import get_swagger_view
# Create your views here.

class YearFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        year = request.query_params.get('year', None)
        if year is not None:
            return queryset.filter(year=year)
        else:
            return queryset


class RegionFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        region = request.query_params.get('region', None)
        if region is not None:
            return queryset.filter(region=region)
        else:
            return queryset


class KeywordFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        keyword = request.query_params.get('keyword', None)
        if keyword is not None:
            k = models.Keyword.objects.select_related().get(word=keyword)
            queryset = k.keywords.all()
            if queryset.count() > 100:
                return queryset[:100]
        return queryset


class LenFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        limit = request.query_params.get('limit', None)
        if limit is not None:
            limit = int(limit)
            if queryset.count() > limit:
                return queryset[: limit]
            else:
                return queryset
        else:
            return queryset


class CountryFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        country = request.query_params.get('country', None)
        if country is not None:
            return queryset.filter(country=country)
        else:
            return queryset

class PeriodFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start = request.query_params.get('start', None)
        end = request.query_params.get('end', None)
        if start is not None and end is not None:
            start = datetime.strptime(start, '%Y%m%d')
            end = datetime.strptime(end, '%Y%m%d')
            queryset = queryset.filter(date__gte=start)
            queryset = queryset.filter(date__lte=end)
            return queryset
        else:
            return queryset


class PolygonFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        p_str = request.query_params.get('ploy', None)
        if p_str is not None:
            poly = Polygon(json.loads(p_str), srid=4326)
            return queryset.filter(location__within=poly)
        return queryset


'''
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
'''


class CountryGeoViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有国家的多边形边界
    retrieve: 查询某一国家的多边形边界
    '''
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountryGeoSerializer
    filter_backends = (RegionFilter, )


class RegionGeoViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有地区的多边形边界
    retrieve: 查询某一地区的多边形边界
    '''
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionGeoSerializer


'''
class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
'''


class AttackViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有袭击类型数据
    retrieve: 返回某一id对应的袭击类型
    '''
    queryset = models.Attack.objects.all()
    serializer_class = serializers.AttackSerializer


class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有武器类型数据
    retrieve: 返回某一id对应的武器类型
    '''
    queryset = models.Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer


class TargetViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有目标类型数据
    retrieve: 返回某一id对应的目标类型
    '''
    queryset = models.Target.objects.all()
    serializer_class = serializers.TargetSerializer


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回所有关键词出现频数数据，使用limit限制返回词个数
    retrieve: 返回某一id对应的关键词词频
    '''
    queryset = models.Keyword.objects.all()
    serializer_class = serializers.KeywordSerializer
    filter_backends = (LenFilter, )


class TDInfoViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回按关键词（keyword）、国家（country）、地区（region）、时间段（start&end）、多边形（poly）筛选得到的袭击详细数据
    retrieve: 返回某一id对应的袭击详细数据
    '''
    queryset = models.TerrorismData.objects.all()
    serializer_class = serializers.TDInfoSerialier
    filter_backends = (KeywordFilter, CountryFilter, PeriodFilter, RegionFilter, PolygonFilter, YearFilter)

    @action(methods=['get'], detail=False)
    def statistics(self, request):
        '''
        返回按过滤字段筛选后的统计数据
        '''
        td_queryset = self.filter_queryset(self.get_queryset())
        weapon = td_queryset.values('weaponType').annotate(count=Count('weaponType')).values('weaponType', 'weaponType__weaponTypeName', 'count').order_by('-count')
        weapon = weapon.annotate(weaponTypeName=F('weaponType__weaponTypeName')).values('weaponType', 'weaponTypeName', 'count')
        attack = td_queryset.values('attackType').annotate(count=Count('attackType')).values('attackType', 'attackType__attackTypeName', 'count').order_by('-count')
        attack = attack.annotate(attackTypeName=F('attackType__attackTypeName')).values('attackType', 'attackTypeName', 'count')
        target = td_queryset.values('targetType').annotate(count=Count('targetType')).values('targetType', 'targetType__targetTypeName', 'count').order_by('-count')
        target = target.annotate(targetTypeName=F('targetType__targetTypeName')).values('targetType', 'targetTypeName', 'count')
        
        # sum_kill = td_queryset.values('numKill').annotate(sumKill=Sum('numKill'))
        sum_kill = td_queryset.aggregate(sum=Sum('numKill'))['sum']
        sum_wound = td_queryset.aggregate(sum=Sum('numWound'))['sum']
        sum_prop = td_queryset.aggregate(sum=Sum('propValue'))['sum']
        return Response({'num': td_queryset.count(), 'kill': sum_kill, 'wound': sum_wound, 'prop': sum_prop, 'attack': attack, 'target': target, 'weapon': weapon})
    
    @action(methods=['get'], detail=False)
    def trend(self, request):
        '''
        返回国家/地区的年袭击数、死伤人数、经济损失趋势
        '''
        td_queryset = self.filter_queryset(self.get_queryset())
        trend = td_queryset.values('year').annotate(count=Count('year'), sumKill=Sum('numKill'), sumWound=Sum('numWound'), sumProp=Sum('propValue')).values('year', 'count', 'sumKill', 'sumWound', 'sumProp')
        return Response(trend.order_by('year'))

    @action(methods=['get'], detail=False)
    def globalStatistics(self, request):
        '''
        返回全球各地区某时段袭击次数、死亡人数、经济损失
        '''
        td_queryset = self.filter_queryset(self.get_queryset())
        gs = td_queryset.values('region').annotate(count=Count('region'), sumKill=Sum('numKill'), sumWound=Sum('numWound'), sumProp=Sum('propValue')).values('region', 'region__regionName', 'count', 'sumKill', 'sumWound', 'sumProp')
        gs = gs.annotate(regionName=F('region__regionName')).values('region', 'regionName', 'count', 'sumKill', 'sumWound', 'sumProp')
        return Response(gs.order_by('region'))

    @action(methods=['get'], detail=False)
    def regionStatistics(self, request):
        '''
        返回某一地区各国家某时段袭击次数、死亡人数、经济损失
        '''
        td_queryset = self.filter_queryset(self.get_queryset())
        gs = td_queryset.values('country').annotate(count=Count('country'), sumKill=Sum('numKill'), sumWound=Sum('numWound'), sumProp=Sum('propValue')).values('country', 'country__countryName', 'count', 'sumKill', 'sumWound', 'sumProp')
        gs = gs.annotate(countryName=F('country__countryName')).values('country', 'countryName', 'count', 'sumKill', 'sumWound', 'sumProp')
        return Response(gs.order_by('country'))


class TDGeneralViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list: 返回按关键词（keyword）、国家（country）、地区（region）、时间段（start&end）、多边形（poly）筛选得到的袭击点位数据
    retrieve: 返回某一id对应的袭击点位数据
    '''
    queryset = models.TerrorismData.objects.all()
    serializer_class = serializers.TDGeoSerializer
    filter_backends = (YearFilter, RegionFilter, CountryFilter, PeriodFilter, KeywordFilter, PolygonFilter)


schema_view = get_swagger_view(title='GTD API', url=None)

