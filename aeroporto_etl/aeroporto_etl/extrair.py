import os
import re

import requests

from constantes import BASE_URL


def get_endpoint(endpoint, endpoint_id=None, params=None):
    headers = {
        "Accept": "application/json",
        "app_id": os.getenv('APP_ID'),
        "app_key": os.getenv('APP_KEY'),
        "ResourceVersion": "v4"
    }

    url = BASE_URL + endpoint

    if endpoint_id:
        url = url + "/" + endpoint_id

    resultado_get = requests.get(url=url, headers=headers, params=None)
    
    numero_paginas = processar_headers_numero_paginas(resultado_get.headers)


def processar_headers_numero_paginas(headers):

    headers_link = headers.get('link')
    if not headers_link:
        return '0'
    
    link_partes = headers_link.split(',')

    exp_regular = r".*page=([0-9]+).*"

    for link_parte in link_partes:
        if 'rel="last"' in link_parte:
            numero = link_parte.split(';')[0]
            numero = re.search(exp_regular, numero)
            
            import ipdb; ipdb.set_trace()
            return numero.groups()[0]
            



if __name__ == "__main__":
    get_endpoint('flights')