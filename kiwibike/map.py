import requests

url = "http://localhost:8000/api/v1/bike/"

with open('template1.html', encoding='utf8') as template_file:
    map_template1 = template_file.read()

with open('template2.html', encoding='utf8') as template_file:
    map_template2 = template_file.read()

with open('template3.html', encoding='utf8') as template_file:
    map_template3 = template_file.read()

data = {
	"lat_a": 12.939440,
	"lon_a": 50.305940,
	"lat_b": 14.437800,
	"lon_b": 50.075539
}
res = requests.post(f"{url}get-route/", data=data)
data = res.json()

coordinates = data["route"]
for l in coordinates:
    l[0], l[1] = l[1], l[0]

center = str(coordinates[0])
coordinates = str(coordinates)


with open('map.html', 'w', encoding='utf8') as output_file:
    output_file.write(map_template1 + center + map_template2 + coordinates + map_template3)