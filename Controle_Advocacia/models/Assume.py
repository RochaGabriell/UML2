import json
from models.Advogado import Advogado
from models.Processo import Processo

class Assume:
    def __init__(self, dataInicio: str, dataFinal: str, processo: Processo) -> None:
        self.__dataInicio = dataInicio
        self.__dataFinal = dataFinal
        self.__processo = processo
        self._dados_Assume = []

    def incluirAdvogado(self, oabAdvogado: dict) -> None: # servem para associar um novo advogado a um processo
        dict_Assume = {
            "__dataInicio": self.__dataInicio,
            "__dataFinal": self.__dataFinal,
            "__processo": self.__processo,
            "oab_Advogado": oabAdvogado
        }
        self._dados_Assume.append(dict_Assume)
        print(json.dumps(dict_Assume, sort_keys=False, indent=4))

    def atualizarAdvogado(self, oab: int) -> None: # atualizar a situação de um advogado, se um advogado deixar um processo
        for dados in self._dados_Assume:
            if oab == dados["oab_Advogado"]:
                return dados

    def pesquisarAdvogado(self, oab: int) -> str: # pesquisar os advogados que participam deum determinado processo
        for dados in self._dados_Assume:
            if oab == dados["oab_Advogado"]:
                return dados