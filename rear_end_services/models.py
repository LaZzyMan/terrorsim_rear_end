from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(verbose_name='国家名', max_length=100)

    def __str__(self):
        return self.country_name


class Attack(models.Model):
    attack_type_id = models.IntegerField(primary_key=True)
    attack_type_name = models.CharField(verbose_name='袭击方式', max_length=100)

    def __str__(self):
        return self.attack_type_name


class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(verbose_name='地区名', max_length=100)

    def __str__(self):
        return self.region_name


class Target(models.Model):
    target_type_id = models.IntegerField(primary_key=True)
    target_type_name = models.CharField(verbose_name='袭击目标', max_length=200)

    def __str__(self):
        return self.target_type_name


class Weapon(models.Model):
    weapon_type_id = models.IntegerField(primary_key=True)
    weapon_type_name = models.CharField(verbose_name='武器类型', max_length=100)

    def __str__(self):
        return self.weapon_type_name


class TerrorismData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    year = models.IntegerField(verbose_name='年份', null=True, db_index=True)
    month = models.IntegerField(verbose_name='月份', null=True, db_index=True)
    day = models.IntegerField(verbose_name='日期', null=True, db_index=True)
    date = models.DateField(verbose_name='时间', null=True)
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                   verbose_name='国家', blank=True, null=True, db_index=True)
    region_id = models.ForeignKey(Region, on_delete=models.SET_NULL,
                                  verbose_name='地区', blank=True, null=True, db_index=True)
    city = models.CharField(verbose_name='城市', null=True, max_length=200)
    summary = models.TextField(verbose_name='事件报道', null=True)
    suicide = models.IntegerField(verbose_name='自杀式袭击', choices=[(0, 'no'), (1, 'yes')], blank=True, db_index=True)
    attack_type = models.ForeignKey(Attack, on_delete=models.SET_NULL,
                                    verbose_name='袭击方式', blank=True, null=True, db_index=True)
    target_type = models.ForeignKey(Target, on_delete=models.SET_NULL,
                                    verbose_name='袭击目标', blank=True, null=True, db_index=True)
    weapon_type = models.ForeignKey(Weapon, on_delete=models.SET_NULL,
                                    verbose_name='武器类型', blank=True, null=True, db_index=True)
    group_name = models.CharField(verbose_name='组织名称', max_length=200, blank=True)
    motive = models.TextField(verbose_name='动机', null=True)
    num_kill = models.IntegerField(verbose_name='死亡人数', null=True)
    num_wound = models.IntegerField(verbose_name='受伤人数', null=True)
    prop_value = models.FloatField(verbose_name='经济损失', null=True)
    prop_comment = models.TextField(verbose_name='损失情况', null=True)
    location = models.PointField(srid=4326, verbose_name='位置', null=True)

    def __str__(self):
        return str(self.id)


class GlobalTerrorism(models.Model):
    verbose_name = '恐怖袭击位置数据'
    id = models.CharField(max_length=50, primary_key=True)
    year = models.CharField(max_length=50, verbose_name='年份')
    month = models.CharField(max_length=50, verbose_name='月份')
    day = models.CharField(max_length=50, verbose_name='日期')
    geom = models.PointField(srid=4326, verbose_name='位置')

    def __str__(self):
        return self.id


class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    mpoly = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

