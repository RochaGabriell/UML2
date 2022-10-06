from models.Processo import Processo

class Vara:
    def __init__(self, descricaoVara: str, processo: Processo) -> None:
        self.__descricaoVara = descricaoVara
        self._dados_Vara = ["Vara do Trabalho", "Vara da Fazenda Pública", "Vara Cível", "Vara criminal"]

    #Métodos referentes ao atributo descricaoVara
    @property
    def descricaoVara(self) -> str:
        return self.__descricaoVara

    @descricaoVara.setter
    def descricaoVara(self, descricao: str) -> None:
        self.__descricaoVara = descricao

    def consultaVara(self, descricao) -> str:
        for vara in self._dados_Vara:
            if descricao == vara.__descricaoVara:
                print(vara)

    def listarVara(self) -> str:
        for vara in self._dados_Vara:
            print(vara)