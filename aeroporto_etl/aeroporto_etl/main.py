from extrair import get_airlines, get_aircraft_types
from salvar import salvar
from transformar import transformar_airlines, transformar_aircraft_types


def main_etl():
    airlines_paginas = get_airlines()
    aircraft_types_paginas = get_aircraft_types()

    airlines = transformar_airlines(airlines_paginas)
    aircraft_types = transformar_aircraft_types(aircraft_types_paginas)

    salvar(
        '../',
        [
            airlines,
            aircraft_types
        ],
        [
            'airlines',
            'aircraft_types', 
        ]
    )
if __name__ == "__main__":
    main_etl()