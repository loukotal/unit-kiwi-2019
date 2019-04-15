import citybikes

from bikesharing.models import Company, Location, Station


def get_companies_locations(networks_list, number_of_networks=5):
    # Expecting client.network as parameter
    companies = {}
    company_list = []
    count = 0
    for n in networks_list:
        if n['company']:
            count += 1
            station_list = []
            for station in list(n.stations):
                # print(station)
                s = {'id': station['id'],
                     'empty_slots': station['empty_slots'],
                     'free_bikes': station['free_bikes'],
                     'latitude': station['latitude'],
                     'longitude': station['longitude'],
                     'name': station['name']
                     }
                station_list.append(s)

            if n['company'][0] not in companies:
                company_list.append(n['company'][0])
                companies[n['company'][0]] = [{'country': n['location']['country'],
                                               'city': n['location']['city'],
                                               'latitude': n['location']['latitude'],
                                               'longitude': n['location']['longitude'],
                                               'stations': station_list
                                               }]
            else:
                companies[n['company'][0]].append({'country': n['location']['country'],
                                                   'city': n['location']['city'],
                                                   'latitude': n['location']['latitude'],
                                                   'longitude': n['location']['longitude'],
                                                   'stations': station_list
                                                   })
            if count >= number_of_networks:
                break
    return companies, company_list


# if __name__ == "__main__":
client = citybikes.Client()
companies, company_list = get_companies_locations(list(client.networks))

for company, locations in companies.items():
    # comp = Company.objects.get_or_create(name=company)

    for location in locations:
        # loc = Location.objects.get_or_create(company_id=comp.id, country=location["country"], lat=location["latitude"],
        #                                      lon=location["longitude"], city=location["city"])
        print(location)

for key in companies.keys():
    comp = Company.objects.get_or_create(name=key)

    for network in company[key]:
        net = Location.objects.get_or_create(lat=network["latitude"], lon=network["longitude"],
                                             country=network["country"],
                                             city=network["city"], company=comp[0].id)

        for station in network["stations"]:
            stat = Station.objects.get_or_create(free_bikes=station["free_bikes"], lon=station["longitude"],
                                                 lat=station["latitude"],
                                                 name=station["name"], location=net[0].id)
