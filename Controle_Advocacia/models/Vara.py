class Vara:
    def __init__(self, descricaoVara: str) -> None:
        self.__descricaoVara = descricaoVara
        self._dados_Vara = []

    #Métodos referentes ao atributo descricaoVara
    @property
    def descricaoVara(self) -> str:
        return self.__descricaoVara

    @descricaoVara.setter
    def descricaoVara(self, descricao: str) -> None:
        self.__descricaoVara = descricao

    def registrarVara(self, self_v) -> None:
        self._dados_Vara.append(self_v)

    def consultaVara(self, descricao: str) -> str:
        for vara in self._dados_Vara:
            if descricao == vara.__descricaoVara:
                return vara.__descricaoVara

    def listarVara(self) -> str:
        for vara in self._dados_Vara:
            print(vara.__descricaoVara)