from typing import Union, Optional
from tratar_dados.puxar_dados import puxar_dados
from tratar_dados.atualizar_dados import atualizar_dados
from estrutura_dados.distrbuidor import Distribuidor


def tratamento_registro_cadastro(*args: tuple) -> Union[Optional, str]:
    """id , nome, cnpj, contato, nivel, nome_pai, pecas_vendidas"""

    dados_vendas, dados_dist = puxar_dados()

    result = verificar_conteudo_dos_dados(args)

    if type(result) == str:
        return result
    if type(result) == Distribuidor:
        dados_dist.append(result)

    atualizar_dados(dados_vendas, dados_dist)

    return 'Sucesso'


def verificar_conteudo_dos_dados(*args: tuple):

    try:
        tratar_id(args[0])
    except Exception as e:
        return e

    try:
        tratar_strs(args[1], args[3])
    except Exception as e:
        return e

    try:
        tratar_cnpj(args[2])
    except Exception as e:
        return e

    try:
        tratar_nivel(args[4])
    except Exception as e:
        return e

    try:
        tratar_nome_pai(args[5])
    except Exception as e:
        return e

    try:
        tratar_float(args[6])
    except Exception as e:
        return e
