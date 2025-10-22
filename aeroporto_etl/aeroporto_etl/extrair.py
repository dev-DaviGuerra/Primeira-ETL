import os
import re
import logging
import time
from pathlib import Path
import requests


from constantes import BASE_URL

DIRETORIO_ATUAL = Path(__file__).parent.parent.parent

ARQUIVO_LOG = DIRETORIO_ATUAL / 'aeroporto.log'

logging.basicConfig(
    filename=ARQUIVO_LOG,
    level= logging.DEBUG,
    format="%(asctime)s %(message)s",
    filemode="w"
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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

    resultados = [] 

    resultado_get = requests.get(url=url, headers=headers, params=None)
    resultado_get.raise_for_status()

    resultados.append(resultado_get.json())

    numero_paginas = processar_headers_numero_paginas(resultado_get.headers)

    while link:=processar_headers_next(resultado_get.headers):
        time.sleep(0.5)
        logger.info(f"Páginas: {numero_paginas}, link: {link}")
        resultado_get = requests.get(url=link, headers=headers, params=None)
        resultado_get.raise_for_status()
        resultados.append(resultado_get.json())

    return resultados




def processar_headers_next(headers):

    headers_link = headers.get('link')

    if not headers_link:
        return None
    
    link_partes = headers_link.split(',')
    regular_exp = r"<(.*)>"

    for link_parte in link_partes:
        if 'rel="next"' in link_parte:
            link = link_parte.split(';')[0]
            link = re.search(regular_exp, link)
            return link.groups()[0]
    

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
            
            return numero.groups()[0]
            



if __name__ == "__main__":
    get_endpoint('flights')