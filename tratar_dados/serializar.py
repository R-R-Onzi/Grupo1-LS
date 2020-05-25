import pickle
from typing import List
from configparser import ConfigParser
from estrutura_dados.distrbuidor import Distribuidor
from estrutura_dados.vendas import Vendas


def serializar_dados(
    dados_vendas: List[Vendas],
    dados_dist: List[Distribuidor],
) -> None:
    """lista de vendas, lista de distribuidores"""

    config = ConfigParser('.config.cfg')
    
    vendas_save_file_path = config.get('serializacao', 'vendas_path')
    dist_save_file_path = config.get('serializacao', 'dist_path')

    make_dump(dados_vendas, vendas_save_file_path)
    make_dump(dados_dist, dist_save_file_path)


# TODO put a log in here
def make_dump(list_to_dump: List, dump_path: str) -> None:
    with open(dump_path, 'wb') as dump_file:
        try:
            pickle.dump(list_to_dump, dump_file)
        except Exception as e:
            print(f'bota um log aqui pelamor de deus\n{e}')
