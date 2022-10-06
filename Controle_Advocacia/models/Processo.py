import json
from models.Pessoa import Pessoa, PessoaFisica, PessoaJuridica
from models.Vara import Vara

class Processo:
    def __init__(self, numeroProcesso: str, aberturaProcesso: str, conclusaoProcesso: str, descricaoProcesso: str, situacaoProcesso: bool, pessoaCliente: PessoaFisica, pessoaContrario: PessoaJuridica, vara: Vara) -> None:
        self.__numeroProcesso = numeroProcesso
        self.__aberturaProcesso = aberturaProcesso
        self.__conclusaoProcesso = conclusaoProcesso
        self.__descricaoProcesso = descricaoProcesso
        self.__situacaoProcesso = situacaoProcesso
        self.__pessoaCliente = pessoaCliente
        self.__pessoaContrario = pessoaContrario
        self.__vara = vara
        self._dados_Processo = []

    def registrarProcesso(self, self_p) -> None:
        self._dados_Processo.append(self_p)

    def consultarProcesso(self, numero: str) -> str:
        for processo in self._dados_Processo:
            if numero == processo.__numeroProcesso:
                dict_Processo = {
                    "__numeroProcesso": processo.__numeroProcesso,
                    "__aberturaProcesso": processo.__aberturaProcesso,
                    "__conclusaoProcesso": processo.__conclusaoProcesso,
                    "__descricaoProcesso": processo.__descricaoProcesso,
                    "__situacaoProcesso": processo.__situacaoProcesso,
                    "__pessoaCliente": processo.__pessoaCliente,
                    "__pessoaContrario": processo.__pessoaContrario,
                    "__vara": processo.__vara
                    }
                # print(json.dumps(dict_Processo, sort_keys=False, indent=4))
                return dict_Processo

    def listarProcesso(self) -> None:
        for processo in self._dados_Processo:
            dict_Processo = {
                "__numeroProcesso": processo.__numeroProcesso,
                "__aberturaProcesso": processo.__aberturaProcesso,
                "__conclusaoProcesso": processo.__conclusaoProcesso,
                "__descricaoProcesso": processo.__descricaoProcesso,
                "__situacaoProcesso": processo.__situacaoProcesso,
                "__pessoaCliente": processo.__pessoaCliente,
                "__pessoaContrario": processo.__pessoaContrario,
                "__vara": processo.__vara
                }
            print(json.dumps(dict_Processo, sort_keys=False, indent=4))

    def atualizarProcesso(self, numero: str) -> int:
        for processo in self._dados_Processo:
            if numero == processo.__numeroProcesso:
                return processo