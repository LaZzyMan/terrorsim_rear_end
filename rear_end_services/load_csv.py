import pandas as pd
import datetime
from random import randint
import numpy as np
from .models import Attack, Target, TerrorismData, Weapon, Country, Region
from django.contrib.gis.geos import Point


def load_country(filename):
    data = pd.read_csv(filename)
    for code, country in zip(data.code, data.country):
        t = Country(country_id=code, country_name=country)
        t.save()
        print('Load ', t)


def load_region(filename):
    data = pd.read_csv(filename)
    for code, region in zip(data.code, data.region):
        t = Region(region_id=code, region_name=region)
        t.save()
        print('Load ', t)


def load_attack(filename):
    data = pd.read_csv(filename)
    for code, attack in zip(data.code, data.attacktype1):
        t = Attack(attack_type_id=code, attack_type_name=attack)
        t.save()
        print('Load ', t)


def load_target(filename):
    data = pd.read_csv(filename)
    for code, target in zip(data.code, data.targtype1):
        t = Target(target_type_id=code, target_type_name=target)
        t.save()
        print('Load ', t)


def load_weapon(filename):
    data = pd.read_csv(filename)
    for code, weapon in zip(data.code, data.weaptype1):
        t = Weapon(weapon_type_id=code, weapon_type_name=weapon)
        t.save()
        print('Load ', t)


def load_td(filename, start=0):
    data = pd.read_csv(filename)
    for i in range(start, data.shape[0]):
        try:
            t = TerrorismData(id=data.eventid[i])
            t.year = data.iyear[i]
            if data.imonth[i] == 0:
                t.month = randint(1, 12)
            else:
                t.month = data.imonth[i]
            if data.iday[i] == 0:
                t.day = randint(1, 28)
            else:
                t.day = data.iday[i]
            date = datetime.date(t.year, t.month, t.day)
            t.date = date
            t.country_id = Country.objects.get(country_id=data.country[i])
            t.region_id = Region.objects.get(region_id=data.region[i])
            t.city = data.city[i]
            t.summary = data.summary[i]
            if not np.isnan(data.suicide[i]):
                t.suicide = data.suicide[i]
            if not np.isnan(data.attacktype1[i]):
                t.attack_type = Attack.objects.get(attack_type_id=data.attacktype1[i])
            if not np.isnan(data.targtype1[i]):
                t.target_type = Target.objects.get(target_type_id=data.targtype1[i])
            if not np.isnan(data.weaptype1[i]):
                t.weapon_type = Weapon.objects.get(weapon_type_id=data.weaptype1[i])
            t.group_name = data.gname[i]
            t.motive = data.motive[i]
            if not np.isnan(data.nkill[i]):
                t.num_kill = data.nkill[i]
            if not np.isnan(data.nwound[i]):
                t.num_wound = data.nwound[i]
            if not np.isnan(data.propvalue[i]):
                t.prop_value = data.propvalue[i]
            t.prop_comment = data.propcomment[i]
            t.location = Point(data.longitude[i], data.latitude[i])
            t.save()
            print('Load ', i)
        except Exception as e:
            raise Exception(i)

def make_1993_data():
    events = TerrorismData.objects.filter(year=1983)
    for event in events:
        event.id = '1993' + event.id[4:]
        event.year = 1993
        event.save()
        print('Load', event)

if __name__ == '__main__':
    # load_country('../terrorism_rear_end/data/country.csv')
    load_td('../terrorism_rear_end/data/data.csv')
