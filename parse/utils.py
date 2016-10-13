# -*- coding: utf-8 -*-
from django.db import IntegrityError
import json
import urllib.request
from parse.models import Region, Country

URL_JSON = 'http://www.test.d-cod.com/eFw3Cefj.json'


def get_data():
    with urllib.request.urlopen(URL_JSON) as json_file:
        dict_from_json = json.loads(json_file.read().decode('utf-8'))
    listy = dict_from_json['data']
    for dicty in listy:
        try:
            region = Region(name=dicty['Регион'])
            region.save()
        except IntegrityError:
            region = Region.objects.get(name=dicty['Регион'])
        country = Country(name=dicty['Страна'], value=dicty['Значение'])
        country.region = region
        country.save()
