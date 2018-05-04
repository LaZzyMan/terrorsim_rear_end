import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, GlobalTerrorism

# Auto-generated `LayerMapping` dictionary for GlobalTerrorism model
gt_mapping = {
    'id': 'eventid',
    'year': 'year',
    'month': 'month',
    'day': 'day',
    'geom': 'POINT',
}
gt_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../terrorism_rear_end/data/terrorism', 'gtd.shp'))


def load_shp(verbose=True):
    lm = LayerMapping(GlobalTerrorism,
                      gt_shp,
                      gt_mapping,
                      transform=False,
                      encoding='iso-8859-1',)
    lm.save(strict=True, verbose=verbose)


def load_csv():
    pass

