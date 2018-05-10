import pandas as pd
import datetime
from random import randint
import numpy as np
from .models import Attack, Target, TerrorismData, Weapon, Country, Region, Keyword
from django.contrib.gis.geos import Point


def load_keyword(filename):
    data = pd.read_csv(filename)
    for id, word, f in zip(data.id, data.word, data.frequency):
        t = Keyword(wordId=id, word=word, frequency=f)
        t.save()
        print('Load', t)


def load_country(filename):
    data = pd.read_csv(filename)
    for code, country in zip(data.code, data.country):
        t = Country(countryId=code, countryName=country)
        t.save()
        print('Load ', t)


def load_region(filename):
    data = pd.read_csv(filename)
    for code, region in zip(data.code, data.region):
        t = Region(regionId=code, regionName=region)
        t.save()
        print('Load ', t)


def load_attack(filename):
    data = pd.read_csv(filename)
    for code, attack in zip(data.code, data.attacktype1):
        t = Attack(attackTypeId=code, attackTypeName=attack)
        t.save()
        print('Load ', t)


def load_target(filename):
    data = pd.read_csv(filename)
    for code, target in zip(data.code, data.targtype1):
        t = Target(targetTypeId=code, targetTypeName=target)
        t.save()
        print('Load ', t)


def load_weapon(filename):
    data = pd.read_csv(filename)
    for code, weapon in zip(data.code, data.weaptype1):
        t = Weapon(weaponTypeId=code, weaponTypeName=weapon)
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
            t.country = Country.objects.get(countryId=data.country[i])
            t.region = Region.objects.get(regionId=data.region[i])
            t.city = data.city[i]
            t.summary = data.summary[i]
            if not np.isnan(data.suicide[i]):
                t.suicide = data.suicide[i]
            if not np.isnan(data.attacktype1[i]):
                t.attackType = Attack.objects.get(attackTypeId=data.attacktype1[i])
            if not np.isnan(data.targtype1[i]):
                t.targetType = Target.objects.get(targetTypeId=data.targtype1[i])
            if not np.isnan(data.weaptype1[i]):
                t.weaponType = Weapon.objects.get(weaponTypeId=data.weaptype1[i])
            t.groupName = data.gname[i]
            t.motive = data.motive[i]
            if not np.isnan(data.nkill[i]):
                t.numKill = data.nkill[i]
            if not np.isnan(data.nwound[i]):
                t.numWound = data.nwound[i]
            if not np.isnan(data.propvalue[i]):
                t.propValue = data.propvalue[i]
            t.propComment = data.propcomment[i]
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

def make_keyword_relation(filename):
    mapping = pd.read_csv(filename)
    for id, text in zip(mapping.eventid, mapping.word_id):
        t = TerrorismData.objects.get(id=id)
        words = text.split()
        for word in words:
            w = Keyword.objects.get(wordId=word)
            t.keywords.add(w)
        print('Load ', t)


if __name__ == '__main__':
    # load_country('../terrorism_rear_end/data/country.csv')
    load_td('../terrorism_rear_end/data/data.csv')
