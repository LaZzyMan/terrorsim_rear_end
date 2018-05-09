import os
from django.contrib.gis.utils import LayerMapping
from .models import Country, Region

# Auto-generated `LayerMapping` dictionary for GlobalTerrorism model
country_mapping = {
    'country_id': 'id',
    'country_name': 'name',
    'region_id': 'regionid',
    'region_name': 'region',
    'boundary': 'MULTIPOLYGON',
}

region_mapping = {
    'region_id': 'regionid',
    'boundary': 'MULTIPOLYGON',
}
gt_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/region', 'region.shp'))


def load_shp(verbose=True):
    lm = LayerMapping(Region,
                      gt_shp,
                      region_mapping,
                      transform=False,
                      encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)


def fit_region_name():
    for obj in Country.objects.all():
        r = Region.objects.get(region_id=obj.region_id)
        r.region_name = obj.region_name
        r.save()
        print(obj.region_name)

def fit_fk():
    for obj in Country.objects.all():
        r = Region.objects.get(region_id=obj.rid)
        obj.region = r
        obj.save()
        print(obj)