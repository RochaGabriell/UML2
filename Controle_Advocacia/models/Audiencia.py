import json
from models.Processo import Processo

class Audiencia:
    def __init__(self, dataAudiencia: str, parecerAudiencia: str, processo: Processo) -> None:
        self.__dataAudiencia = dataAudiencia
        self.__parecerAudiencia = parecerAudiencia
        self.__processo = processo
        self._dados_Audiencia = []

    def registrarAudiencia(self, self_a) -> int:
        self._dados_Audiencia.append(self_a)

    def consultarAudiencia(self, processo: str) -> str:
        for audiencia in self._dados_Audiencia:
            if processo == audiencia.__processo["__numeroProcesso"]:
                dict_Audiencia = {
                    "__dataAudiencia": audiencia.__dataAudiencia,
                    "__parecerAudiencia": audiencia.__parecerAudiencia,
                    "__processo": audiencia.__processo
                }
                return dict_Audiencia

    def listarAudiencia(self) -> None:
        for audiencia in self._dados_Audiencia:
            dict_Audiencia = {
                "__dataAudiencia": audiencia.__dataAudiencia,
                "__parecerAudiencia": audiencia.__parecerAudiencia,
                "__processo": audiencia.__processo
            }
            print(json.dumps(dict_Audiencia, sort_keys=False, indent=4))