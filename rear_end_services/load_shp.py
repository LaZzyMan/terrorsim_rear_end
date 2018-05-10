import os
from django.contrib.gis.utils import LayerMapping
from .models import Country, Region

# Auto-generated `LayerMapping` dictionary for GlobalTerrorism model
country_mapping = {
    'countryId': 'id',
    'countryName': 'name',
    'regionId': 'regionid',
    'regionName': 'region',
    'boundary': 'MULTIPOLYGON',
}

region_mapping = {
    'regionId': 'regionid',
    'boundary': 'MULTIPOLYGON',
}
gt_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/country', 'countries.shp'))


def load_shp(verbose=True):
    lm = LayerMapping(Country,
                      gt_shp,
                      country_mapping,
                      transform=False,
                      encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)


def fit_region_name():
    for obj in Country.objects.all():
        r = Region.objects.get(regionId=obj.regionId)
        r.regionName = obj.region_name
        r.save()
        print(obj.region_name)

def fit_fk():
    for obj in Country.objects.all():
        r = Region.objects.get(regionId=obj.rid)
        obj.region = r
        obj.save()
        print(obj)
