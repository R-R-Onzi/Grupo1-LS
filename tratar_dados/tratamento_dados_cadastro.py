from tratar_dados.puxar_dados import puxar_dados
from tratar_dados.atualizar_dados import atualizar_dados
from estrutura_dados.distrbuidor import Distribuidor
from tratar_dados.erro_tratamento import ErroTratamento


def tratamento_registro_cadastro(*args):
    """nome, cnpj, contato, nivel, nome_pai, pecas_vendidas"""

    dados_vendas, dados_dist = puxar_dados()

    result = verificar_conteudo_dos_dados(dados_dist, *args)

    if type(result) == ErroTratamento:
        return result.get_msg()
    if type(result) == Distribuidor:
        dados_dist.append(result)
        atualizar_dados(dados_vendas, dados_dist)

    return 'Sucesso'


def verificar_conteudo_dos_dados(
    dados_dist: list,
    *args: tuple,
):
    print(args[0])
    try:
        tratar_nome(args[0])
    except ErroTratamento as e:
        return e

    try:
        tratar_cnpj(args[1])
    except ErroTratamento as e:
        return e

    try:
        tratar_nivel(args[3])
    except ErroTratamento as e:
        return e

    try:
        tratar_nome_pai(args[4], dados_dist)
    except ErroTratamento as e:
        return e

    try:
        tratar_float(args[5])
    except ErroTratamento as e:
        return e

    return Distribuidor(args)


def tratar_id(dist_id, dados_dist) -> None:

    try:
        dist_id = int(dist_id)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o id. Digitou Corretamente?'
        )

    for dist in dados_dist:
        if dist.get_dist_id() == id:
            raise ErroTratamento(
                'Id Já inserido'
            )


def tratar_nome(to_be_string) -> None:

    try:
        to_be_string = str(to_be_string)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o nome. Digitou Corretamente?'
        )

    to_be_string = str(to_be_string)


def tratar_cnpj(cnpj: str):

    cnpj_str = cnpj
    try:
        cnpj = int(cnpj)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o cnpj. Digitou Corretamente?'
        )

    algorismos = list(cnpj_str)
    if len(algorismos) > 14:
        raise ErroTratamento(
            'Não foi possivel tratar o cnpj. Digitou Corretamente?'
        )
    sobra = cpf_iter(algorismos, 11)

    if sobra < 2:
        if not int(algorismos[12]) == 0:
            raise ErroTratamento(
                'Não foi possivel tratar o cnpj. Digitou Corretamente?'
            )
    if not int(algorismos[12]) == 11 - sobra:
        raise ErroTratamento(
            'Não foi possivel tratar o cnpj. Digitou Corretamente?'
        )

    sobra = cpf_iter(algorismos, 13)

    if sobra < 2:
        if not int(algorismos[13]) == 0:
            raise ErroTratamento(
                'Não foi possivel tratar o cnpj. Digitou Corretamente?'
            )
    if not int(algorismos[13]) == 11 - sobra:
        raise ErroTratamento(
            'Não foi possivel tratar o cnpj. Digitou Corretamente?'
        )


def cpf_iter(algorismos: list, start: int):
    soma = 0
    j = 2
    for i in range(start, 0, -1):
        soma += int(algorismos[i]) * j
        j += 1
        if j == 10:
            j = 2
    return soma % (start + 1)


def tratar_nivel(nivel: str):

    niveis_list = []
    with open('.niveis', 'r') as niveis_file:
        niveis_list = niveis_file.readlines()

    if not nivel.upper() in niveis_list:
        raise ErroTratamento(
            'Não foi possivel Encontrar o nivel inserido'
        )


def tratar_nome_pai(nome_pai, dados_dist: list):

    nome_pai = nome_pai.upper()

    for distribuidor in dados_dist:
        if distribuidor.get_nome_pai() == nome_pai:
            return
    raise ErroTratamento(
        'Não foi possivel Encontrar o nome do pai, Digitou Corretamente'
    )


def tratar_float(to_be_float: str):

    try:
        to_be_float = float(to_be_float)
    except Exception:
        raise ErroTratamento(
            'Não foi possivel tratar o nome. Digitou Corretamente?'
        )
