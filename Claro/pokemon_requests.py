from xmlrpc.client import ResponseError
import requests
import json
import xml.etree.ElementTree as ET

URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():

    requets_soap = read_xml_request('requests.xml')
    pokemon_to_search = get_pokemon_for_requests(requets_soap)

    data_final = separa_consulta_x_nombres(pokemon_to_search)

    return data_final

def read_xml_request(path:str):
    '''
    input: str = path o ruta donde se encuentra el archivo xml
    para hacer la consulta Soap.
    output: xml.tree = un objeto de tipo xml.tree con la informacion
    que se desea consultar.
    '''
    tree = ET.parse(path)
 
    root = tree.getroot()

    return root

def get_pokemon_for_requests(xml_requests):
    '''
    input: xml.tree = recibe el elemento xml con la consulta
    soap mencionada en el problema
    output: list = una lista de strings con los pokemones a consultar.

    Este metodo extrae del archivo xml los string de los pokemones que
    se desean consultar.
    '''

    pokemons_search = []

    pokemon_elements = xml_requests[0].findall('list')

    for i in pokemon_elements:
        pokemons_search.append(i[0].text)

    return pokemons_search

def pokemon_data(pokemon:str, url = URL):

    '''
    input pokemon:str = pokemon a buscar en la API
    input url:str = por default es el link del endpoint de la
    API a consultar
    output: str = un string de formato diccionario (o json) 
    con la respuesta de la API. 

    Crea el request a la API y devuelve la respuesta
    en formato string
    '''

    response = requests.get('URL'+pokemon)

    raw_data = response.json()

    return (raw_data)

def separa_consulta_x_nombres(lista_pokemones):

    '''
    input: list = lista compuesta por strings con el nombre
    de cada pokemon a buscar

    output: list = lista compuesta por la información de cada pokemon

    Esta funcion itera por la lista de pokemones obtenida del archivo XML
    y pasa cada nombre por la funcion pokemon_data() para obtener la info
    de cada criatura. Al final devuelve una lista con los pokemon que
    existen en el endpoint.
    Manejo de excepciones, en el caso de tener respuesta 400 por parte
    del endpoint continua con la siguiente iteración.
    '''

    pokemon_data_lst = []

    for i in lista_pokemones:
        if '|' not in i:
            
            try:
                pokemon_data_raw = pokemon_data(i)
                data = get_pokemon_data(pokemon_data_raw)
                data['pokemon'] = i
                pokemon_data_lst.append(data)

            except:
                pass

        else:
            new_i = i.replace(" ", "")
            new_i = i.split("|")
            for j in new_i:
                try:
                    pokemon_data_raw = pokemon_data(j)
                    data = get_pokemon_data(pokemon_data_raw)
                    data['pokemon'] = j
                    pokemon_data_lst.append(data)
    
                except:
                    pass

    return pokemon_data_lst         

def get_pokemon_data(response_api:dict):

    '''
    input: dict = diccionario con toda la data de un pokemon
    output: dict = diccionario solo con la data requerida para
    el problema.

    Esta función toma el json que responde la API y extrae
    solo la informacion de id, base expirience, stats name y stats url
    para solo devolver y manejar esta info.
    '''

    id = response_api['id']
    expirience = response_api['base_experience']

    stats = response_api['stats']

    stat_name = []
    stat_url = []

    for i in stats:
        stat_name.append(i['stat']['name'])
        stat_url.append(i['stat']['url'])

    nuevo_dict = {
                    'id': id,
                    'expirience': expirience,
                    'stat_name': stat_name,
                    'stat_url': stat_url
                }
    
    return nuevo_dict

if __name__ == '__main__':
    
    solucion = main()
    
    with open(r'pokemon_data.txt', 'w') as fp:
        for item in solucion:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')
