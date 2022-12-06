import xml.etree.cElementTree as ET

def main():
    pokemones = obtener_pokemones()
    crear_request(pokemones)

def obtener_pokemones():
    '''
    input: str = texto ingresado por el usuario
    output: list = lista de strings. Cada elemento es un pokemon a
    consultar o una serie de nombres que un pokemon podr[ia llegar
    a tener.
    
    Con esta funcion se obtienen los pokemones que se quieren
    consultar eventualmente en la API del problema.
    Inicialmente le pide al usuario que indique que pokemon quiere
    consultar y por medio de un loop le pide confirmacion para continuar
    el proceso o agregar pokemones para la consulta
    '''
    lista_consultar = []

    primer_input = input('Que pokemon quieres consultar?: ')
    lista_consultar.append(primer_input)

    segundo_input = input('Quieres contultar otro pokemon? Y/N: ')

    opcion = respuesta_y(segundo_input)

    while opcion == 'Y':
        otro_input = input('Que pokemon quieres consultar?: ')
        lista_consultar.append(otro_input)
        segundo_input = input('Quieres contultar otro pokemon? Y/N: ')
        opcion = respuesta_y(segundo_input)


    return lista_consultar

def respuesta_y(respuesta):
    '''
    Como es posible que la confirmacion del usuario no siga
    al pie de la letra las instrucciones del programa
    con esta funcion se manejan algunas excepciones
    '''
    posibles_resp = ['Y', 'y', 'Yes', 'yes', 'si', 'Si', 'YES']

    if respuesta in posibles_resp:
        respuesta = 'Y'

    return respuesta

def crear_request(pokemones_request:list):

    '''
    input: list = una lista cualquiera compuesta por strings de nombres
    de pokemones.

    output: un archivo xml listo para ser usado en un servicio SOAP
    con el formato indicado en el problema.
    '''

    string_lst = ['<BuscarPokemon><pokemones>']

    for i in pokemones_request:
        new_list = f'<list><nombre>{i}</nombre></list>'
        string_lst.append(new_list)

    string_lst.append('</pokemones></BuscarPokemon>')

    string_requests = ''.join(string_lst)

    root = ET.fromstring(string_requests)
    arbol = ET.ElementTree(root)
    arbol.write("requests.xml")

if __name__ == '__main__':
    main()