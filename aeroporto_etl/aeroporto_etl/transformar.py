def transformar_airlines(airlines_paginas):

    resultados = []
    airlines = []

    for pagina in airlines_paginas:
        airlines.extend(pagina.get('airlines'))

    for airline in airlines:
        resultados.append(
            {
            "iata": airline.get('iata'),
            "icao": airline.get('icao'),
            "nvls": airline.get('nvls'),
            "name": airline.get('publicName')
            }
        )
    
    return resultados

def transformar_aircraft_types(aircraft_types_paginas):

    resultados = []
    aircraft_types = []

    for pagina in aircraft_types_paginas:
        aircraft_types.extend(pagina.get('aircraftTypes'))

    for aircraft in aircraft_types:
        resultados.append(
            {
            "iataMain": aircraft.get('iataMain'),
            "iataSub": aircraft.get('iataSub'),
            "description": aircraft.get('longDescription')
            }
        )

    return resultados

def transformar_destinations(destinations_paginas):
    
    resultados = []
    destinations = []

    for pagina in destinations_paginas:
        destinations.extend(pagina.get('destinations'))

    for destination in destinations:
        name = destination.get('publicName')
        if name:
            name = name.get('english')
        resultados.append(
            {
            "name": name,
            "country": destination.get('country'),
            "iata": destination.get('iata'),
            "city": destination.get('city')
            }
        )
    
    return resultados
