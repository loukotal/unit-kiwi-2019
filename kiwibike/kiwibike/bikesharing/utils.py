# TODO: Honzův kód

from requests import get
import requests
import json
from django.conf import settings


def airport_coordinates(key, value):
    base_url = "https://api.skypicker.com/locations?"
    params = "type=general&key={}&value={}".format(key, value)
    url = base_url + params
    data = get(url).json()
    # coordinates = list(data['locations'][0]['location'].values())
    coordinates = data["locations"][0]["location"]
    return coordinates


import ssl


class mapbox:
    def __init__(self, *args):
        self.args = args
        self.data = self.get_raw_data()
        self.geojson = self.geojson()
        self.steps = self.steps()

    def get_raw_data(self):
        token = '?access_token=pk.eyJ1Ijoic3RhcmFwYXJ0YSIsImEiOiJjanVpM3p5ZjIxMzgxNDNwaXNpYmJ2cGMyIn0.coQL-jzkpCG9Q_aFsj3cBw'
        steps = '&steps=true'
        geometry = '&geometries=geojson'
        overview = '&overview=simplified'
        coordinates = '%3B'.join([str(lat) + '%2C' + str(lon) for lat, lon in self.args])
        url = 'https://api.mapbox.com/directions/v5/mapbox/cycling/{}.json{}{}{}{}'.format(coordinates, token, steps,
                                                                                           geometry, overview)
        data = requests.get(url).json()
        return data

    def geojson(self):
        geojson_data = self.data['routes'][0]['geometry']['coordinates']
        geojson_data = [[lat, lon] for lon, lat in geojson_data]
        return geojson_data

    def steps(self):
        steps = self.data['routes'][0]['legs'][0]['steps']
        return steps


url = 'https://api.foursquare.com/v2/venues/search'


# map_data = mapbox((12.939440, 50.305940), (14.437800, 50.075539)).geojson


def get_poi(map_data, radius="1000", limit=5):
    points = []

    for x in map_data:
        points.append(f"{x[0]},{x[1]}")

    params = dict(
        client_id=settings.FSQR_CLIENT_ID,
        client_secret=settings.FSQR_CLIENT_SECRET,
        radius=str(radius),
        v='20180323',
        categoryId='50aaa49e4b90af0d42d5de11,4bf58dd8d48988d181941735',
        limit=limit,
        intent='browse'
    )
    points_of_interest = set()
    for point in points:
        params['ll'] = point
        resp = requests.get(url=url, params=params)

        data = json.loads(resp.text)
        for x in data['response']['venues']:
            points_of_interest.add(f"{x['location']['lat']}\n{x['location']['lng']}\n{x['name']}\n{x['categories'][0]['name']}\n")
    # for i in points_of_interest:
    # print(i)
    return points_of_interest
