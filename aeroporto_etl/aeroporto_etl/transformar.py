


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