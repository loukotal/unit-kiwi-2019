import citybikes

from bikesharing.models import Company, Location, Station


def get_companies_locations(networks_list):
    jnets = []
    for net in networks_list:
        jnets.append(eval(str(net)))
    companies = {}
    company_list = []
    for n in jnets:
        if n['company']:
            if n['company'][0] not in companies:
                company_list.append(n['company'][0])
                companies[n['company'][0]] = [{'country': n['location']['country'],
                                               'city': n['location']['city'],
                                               'latitude': n['location']['latitude'],
                                               'longitude': n['location']['longitude']
                                               }]
            else:
                companies[n['company'][0]].append({'country': n['location']['country'],
                                                   'city': n['location']['city'],
                                                   'latitude': n['location']['latitude'],
                                                   'longitude': n['location']['longitude']
                                                   })
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
        net = Location.objects.get_or_create(lat=network["latitude"], lon=network["longitude"], country=network["country"],
                                         city=network["city"], company=comp[0].id)

        for station in network["stations"]:
            stat = Station.objects.get_or_create(free_bikes=station["free_bikes"], lon=station["longitude"], lat=station["latitude"],
                                                 name=station["name"], location=net[0].id)