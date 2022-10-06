import json
from models.Processo import Processo

class Custa:
    def __init__(self, dataCusta: str, descricaoCusta: str, valorCusta: float, processo: Processo) -> None:
        self.__dataCusta = dataCusta
        self.__descricaoCusta = descricaoCusta
        self.__valorCusta = valorCusta
        self.__processo = processo
        self._dado_Custa= []

    def registarCusta(self, self_c) -> None:
        self._dado_Custa.append(self_c)

    def consultarCusta(self, descricao) -> str:
        for custa in self._dado_Custa:
            if descricao == custa.__descricaoCusta:
                dict_Custa = {
                    "__dataCusta": custa.__dataCusta,
                    "__descricaoCusta": custa.__descricaoCusta,
                    "__valorCusta": custa.__valorCusta,
                    "__processo": custa.__processo
                }
                return dict_Custa

    def listarCusta(self) -> None:
        for custa in self._dado_Custa:
            dict_Custa = {
                "__dataCusta": custa.__dataCusta,
                "__descricaoCusta": custa.__descricaoCusta,
                "__valorCusta": custa.__valorCusta,
                "__processo": custa.__processo
            }
            print(json.dumps(dict_Custa, sort_keys=False, indent=4))