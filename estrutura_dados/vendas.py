import datetime


class Vendas(object):
    def __init__(self, *args):
        """data, valor venda, id distribuidor"""
        self._data: datetime = args[0]
        self._valor_venda: float = args[1]
        self._id_distribuidor: int = args[2]

    def get_data(self):
        return self._data

    def get_valor_venda(self):
        return self._valor_venda

    def get_id_distribuidor(self):
        return self._id_distribuidor
