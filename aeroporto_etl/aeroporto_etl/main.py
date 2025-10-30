from extrair import get_airlines, get_aircraft_types, get_destinations
from salvar import salvar
from transformar import transformar_airlines, transformar_aircraft_types, transformar_destinations


def main_etl():
    ##airlines_paginas = get_airlines()
    ##aircraft_types_paginas = get_aircraft_types()
    destinations_paginas = get_destinations()

    ##airlines = transformar_airlines(airlines_paginas)
    ##aircraft_types = transformar_aircraft_types(aircraft_types_paginas)
    destinations = transformar_destinations(destinations_paginas)

    salvar(
        '../',
        [
            destinations,
        ],
        [
            'destinations'
        ]
    )
if __name__ == "__main__":
    main_etl()