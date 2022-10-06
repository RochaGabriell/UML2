class Tribunal:
    def __init__(self, denominacaoTribunal: str, enderecoTribunal: str) -> None:
        self.__denominacaoTribunal = denominacaoTribunal
        self.__enderecoTribunal = enderecoTribunal
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
                    "__enderecoTribunal": tribunal.__enderecoTribunal
                }
                return dict_Tribunal

    def listarTribunal(self) -> None:
        for tribunal in self._dados_Tribunal:
            dict_Tribunal = {
                "__denominacaoTribunal": tribunal.__denominacaoTribunal,
                "__enderecoTribunal": tribunal.__enderecoTribunal
            }
            print(dict_Tribunal)

tribunal = Tribunal("STF", "Praça dos Três Poderes - Brasília, DF, 70175-900")
tribunal1 = Tribunal("TSE", "R. Percílio Santana, 266, Formosa do Rio Preto - BA, 47990-000")
tribunal2 = Tribunal("STJ", "SAFS - Setor de Administração Federal Sul Quadra 06, Trecho III, Lote 01 - Asa Sul, Brasília - DF, 70095-900")
tribunal3 = Tribunal("CJF", "St. de Clubes Esportivos Sul Trecho 3 - Asa Sul, Brasília - DF, 70200-003")

tribunal.registrarTribunal(tribunal)
tribunal.registrarTribunal(tribunal1)
tribunal.registrarTribunal(tribunal2)
tribunal.registrarTribunal(tribunal3)

# print(tribunal.consultarTribunal("TSE"))

tribunal.listarTribunal()