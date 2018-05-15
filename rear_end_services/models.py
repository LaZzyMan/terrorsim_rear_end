from django.contrib.gis.db import models
# Create your models here.


class Region(models.Model):
    regionId = models.IntegerField(primary_key=True)
    regionName = models.CharField(verbose_name='地区名', max_length=100, null=True)
    boundary = models.MultiPolygonField(verbose_name='边界', srid=4326)

    def __str__(self):
        return self.regionName


class Country(models.Model):
    countryId = models.IntegerField(primary_key=True)
    countryName = models.CharField(verbose_name='国家名', max_length=100)
    boundary = models.MultiPolygonField(verbose_name='边界', srid=4326)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, verbose_name='地区', blank=True, null=True, db_index=True, related_name='countryRegion')
    # rid = models.IntegerField(null=True)

    def __str__(self):
        return self.countryName


class Attack(models.Model):
    attackTypeId = models.IntegerField(primary_key=True)
    attackTypeName = models.CharField(verbose_name='袭击方式', max_length=100)

    def __str__(self):
        return self.attackTypeName


class Target(models.Model):
    targetTypeId = models.IntegerField(primary_key=True)
    targetTypeName = models.CharField(verbose_name='袭击目标', max_length=200)

    def __str__(self):
        return self.targetTypeName


class Weapon(models.Model):
    weaponTypeId = models.IntegerField(primary_key=True)
    weaponTypeName = models.CharField(verbose_name='武器类型', max_length=100)

    def __str__(self):
        return self.weaponTypeName


class Keyword(models.Model):
    wordId = models.IntegerField(primary_key=True)
    word = models.CharField(verbose_name='关键词', max_length=50, db_index=True)
    frequency = models.IntegerField(verbose_name='出现次数')

    def __str__(self):
        return self.word


class TerrorismData(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    year = models.IntegerField(verbose_name='年份', null=True, db_index=True)
    month = models.IntegerField(verbose_name='月份', null=True, db_index=True)
    day = models.IntegerField(verbose_name='日期', null=True, db_index=True)
    date = models.DateField(verbose_name='时间', null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL,
                                   verbose_name='国家', blank=True, null=True, db_index=True, related_name='country')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL,
                                  verbose_name='地区', blank=True, null=True, db_index=True, related_name='region')
    city = models.CharField(verbose_name='城市', null=True, max_length=200)
    summary = models.TextField(verbose_name='事件报道', null=True)
    suicide = models.IntegerField(verbose_name='自杀式袭击', choices=[(0, 'no'), (1, 'yes')], blank=True, db_index=True)
    attackType = models.ForeignKey(Attack, on_delete=models.SET_NULL,
                                    verbose_name='袭击方式', blank=True, null=True, db_index=True, related_name='attack')
    targetType = models.ForeignKey(Target, on_delete=models.SET_NULL,
                                    verbose_name='袭击目标', blank=True, null=True, db_index=True, related_name='target')
    weaponType = models.ForeignKey(Weapon, on_delete=models.SET_NULL,
                                    verbose_name='武器类型', blank=True, null=True, db_index=True, related_name='weapon')
    groupName = models.CharField(verbose_name='组织名称', max_length=200, blank=True)
    motive = models.TextField(verbose_name='动机', null=True)
    numKill = models.IntegerField(verbose_name='死亡人数', null=True)
    numWound = models.IntegerField(verbose_name='受伤人数', null=True)
    propValue = models.FloatField(verbose_name='经济损失', null=True)
    propComment = models.TextField(verbose_name='损失情况', null=True)
    keywords = models.ManyToManyField(Keyword, related_name='keywords', blank=True, null=True, db_index=True)
    location = models.PointField(srid=4326, verbose_name='位置', null=True)

    def __str__(self):
        return str(self.id)


