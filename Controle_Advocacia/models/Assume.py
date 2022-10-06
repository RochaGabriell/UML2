import json
from Advogado import Advogado, advogado

class Assume:
    def __init__(self, dataInicio: str, dataFinal: str) -> None:
        self.__dataInicio = dataInicio
        self.__dataFinal = dataFinal
        self._dados_Assume = []

    def incluirAdvogado(self) -> None: # servem para associar um novo advogado a um processo
        oab = 1005490
        dict_consulta = advogado.consultaAdvogado(oab)
        dict_Assume = {
            "__dataInicio": self.__dataInicio,
            "__dataFinal": self.__dataFinal,
            "Advogado": dict_consulta
        }
        self._dados_Assume.append(dict_Assume)
        print(json.dumps(dict_Assume, sort_keys=False, indent=4))

    def atualizarAdvogado(self, oab: int) -> None: # atualizar a situação de um advogado, se um advogado deixar um processo
        oab = 1005490
        for dados in self._dados_Assume:
            if oab == dados["Advogado"]["__oabAdvogado"]:
                return dados

    def pesquisarAdvogado(self, oab: int) -> str: # pesquisar os advogados que participam deum determinado processo
        for dados in self._dados_Assume:
            if oab == dados["Advogado"]["__oabAdvogado"]:
                return dados["Advogado"]

assume = Assume("05/10/2022", "12/12/2022")
assume.incluirAdvogado()
assume.pesquisarAdvogado(1005490)
assume.atualizarAdvogado(1005490)