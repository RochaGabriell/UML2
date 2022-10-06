import json
from models.Vara import Vara

class Tribunal:
    def __init__(self, denominacaoTribunal: str, enderecoTribunal: str, vara: Vara) -> None:
        self.__denominacaoTribunal = denominacaoTribunal
        self.__enderecoTribunal = enderecoTribunal
        self.__vara = vara
        self._dados_Tribunal = []

    #Métodos referentes ao atributo denominacaoTribunal
    @property
    def denominacaoTribunal(self) -> str:
        return self.__denominacaoTribunal
    
    @denominacaoTribunal.setter
    def denominacaoTribunal(self, denomicacao: str) -> None:
        self.__denominacaoTribunal = denomicacao
    
    #Métodos referentes ao atributo enderecoTribunal
    @property
    def enderecoTribunal(self) -> str:
        return self.__enderecoTribunal

    @enderecoTribunal.setter
    def enderecoTribunal(self, endereco: str) -> None:
        self.__enderecoTribunal = endereco

    def registrarTribunal(self, self_t) -> None:
        self._dados_Tribunal.append(self_t)

    def consultarTribunal(self, denomicacao: str) -> str:
        for tribunal in self._dados_Tribunal:
            if denomicacao == tribunal.__denominacaoTribunal:
                dict_Tribunal = {
                    "__denominacaoTribunal": tribunal.__denominacaoTribunal,
                    "__enderecoTribunal": tribunal.__enderecoTribunal,
                    "__vara": tribunal.__vara
                }
                return dict_Tribunal

    def listarTribunal(self) -> None:
        for tribunal in self._dados_Tribunal:
            dict_Tribunal = {
                "__denominacaoTribunal": tribunal.__denominacaoTribunal,
                "__enderecoTribunal": tribunal.__enderecoTribunal,
                "__vara": tribunal.__vara
            }
            print(json.dumps(dict_Tribunal, sort_keys=False, indent=4))