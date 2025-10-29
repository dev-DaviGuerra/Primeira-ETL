from extrair import get_airlines
from salvar import salvar
from transformar import transformar_airlines


def main_etl():
    airlines_paginas = get_airlines()

    airlines = transformar_airlines(airlines_paginas)

    salvar(
        '../',
        [
            airlines
        ],
        [
            'airline', 
        ]
    )
if __name__ == "__main__":
    main_etl()