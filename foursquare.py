# simple request to get places around exact lat and lng
import ssl
import json
import requests
url = 'https://api.foursquare.com/v2/venues/explore'


# params documentation https://developer.foursquare.com/docs/api/venues/search
params = dict(
  client_id='ID',
  client_secret='SECRET',
  radius='2500',
  v='20180323',
  ll='50.1056,14.3897',
  query='coffee',
  limit=10
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

# printing just the names, structure is pretty complicated, some online json reader recommended
for x in data['response']['groups'][0]['items']:
    print(x['venue']['name'])

# saving whole json for later
f = open("response.txt",'+w')
f.write(json.dumps(data))

# useful stuff that we can get for each place :
# exact formatted address under ['venue']['location']['formattedAddress']
# lat and lng under ['venue']['location']['lat'] and ['venue']['location']['lng']
