import json
import xml.etree.cElementTree as ET

def main():
    data_lst = open_data_list('pokemon_data.txt')
    final_lst = organizar_data(data_lst)

    response = crear_response(final_lst)

    return response

def open_data_list(path:str):

    '''
    input: str = path donde se encuentra el archivo co nla información
    de cada pokemon

    output: lst = lista con cada elemento como información necesaria
    de cada pokemon.
    '''

    data_lst = []

    with open(path, 'r') as fp:
        for line in fp:
            x = line[:-1]

            data_lst.append(x)

    return data_lst

def organizar_data(lst_pokemon:list):

    '''
    input: list = lista donde cada elemento es la informacion de cada
    pokemon

    outpur: str = string para generar el archivo XML

    Esta funcion itera la lista con elementos con informacion de cada
    pokemon y la organiza en un string con la forma del archivo xml
    '''

    final_str_lst = ['<RespuestaPokemon><Mensaje></Mensaje><pokemones>']

    for i in lst_pokemon:

        final_str_lst.append('<list>')
        new_i = i.replace("'", '"')
        i_dict = json.loads(new_i)
        
        id = i_dict['id']
        nombre = i_dict['pokemon']
        expirience = i_dict['expirience']

        final_str_lst.append(f'<id>{id}</id>')
        final_str_lst.append(f'<nombre>{nombre}</nombre>')
        final_str_lst.append(f'<expirience>{expirience}</expirience>')

        for j in i_dict['stat_name']:
            for k in i_dict['stat_url']:
                stat_str = f'<stats><name>{j}</name><url>{k}</url></stats>'
                final_str_lst.append(stat_str)

        final_str_lst.append('</list>')

    final_str_lst.append('</pokemones></RespuestaPokemon>')
    
    return final_str_lst

def crear_response(data_organizada:list):

    '''
    input: str = string con la forma del archivo xml

    esta funcion toma el string con la forma de xml, lo convierte 
    a un objeto xml.tree y lo guarda en la carpeta de ejecución.
    '''
    string_requests = ''.join(data_organizada)

    root = ET.fromstring(string_requests)
    arbol = ET.ElementTree(root)
    arbol.write("response.xml")

if __name__ == '__main__':
    main()