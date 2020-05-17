import pickle
from typing import List, Tuple
from configparser import ConfigParser
from estrutura_dados.distrbuidor import Distribuidor
from estrutura_dados.vendas import Vendas


def puxar_dados() -> Tuple[List[Vendas], List[Distribuidor]]:

    config = ConfigParser('.config_data')

    vendas_save_file_path = config.get('serializacao', 'vendas_path')
    dist_save_file_path = config.get('serializacao', 'dist_path')

    lista_de_vendas = load_data_list(vendas_save_file_path)
    lista_de_dist = load_data_list(dist_save_file_path)

    return lista_de_vendas, lista_de_dist


def load_data_list(load_path: str) -> List:

    lista_objeto = list()

    with open(load_path, 'rb') as load_file:
        try:
            lista_objeto = pickle.load(load_file)
        except Exception as e:
            print(f'bota um log aqui pelamor de deus\n{e}')

    return lista_objeto
