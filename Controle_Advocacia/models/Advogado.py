import json

class Advogado:
    def __init__(self, oabAdvogado: int, nomeAdvogado: str, enderecoAdvogado: str, telefoneAdvogado: str, bairroAdvogado: str, cepAdvogado: str, emailAdvogado: str) -> None:
        self.__oabAdvogado = oabAdvogado
        self.__nomeAdvogado = nomeAdvogado
        self.__enderecoAdvogado = enderecoAdvogado
        self.__telefoneAdvogado = telefoneAdvogado
        self.__bairroAdvogado = bairroAdvogado
        self.__cepAdvogado = cepAdvogado
        self.__emailAdvogado = emailAdvogado
        self._dados_Advogado = []

    #Métodos referentes ao atributo oabAdvogado
    @property
    def oabAdvogado(self) -> int:
        return self.__oabAdvogado

    @oabAdvogado.setter
    def oabAdvogado(self, oab: int) -> None:
        self.__oabAdvogado = oab

    #Métodos referentes ao atributo nomeAdvogado
    @property
    def nomeAdvogado(self) -> str:
        return self.__nomeAdvogado

    @nomeAdvogado.setter
    def nomeAdvogado(self, nome: str) -> None:
        self.__nomeAdvogado = nome

    #Métodos referentes ao atributo enderecoAdvogado
    @property
    def enderecoAdvogado(self) -> str:
        return self.__enderecoAdvogado

    @enderecoAdvogado.setter
    def enderecoAdvogado(self, endereco: str) -> None:
        self.__enderecoAdvogado = endereco

    #Métodos referentes ao atributo telefoneAdvogado
    @property
    def telefoneAdvogado(self) -> str:
        return self.__telefoneAdvogado

    @telefoneAdvogado.setter
    def telefoneAdvogado(self, telefone: str) -> None:
        self.__telefoneAdvogado = telefone

    #Métodos referentes ao atributo bairroAdvogado
    @property
    def bairroAdvogado(self) -> str:
        return self.__bairroAdvogado
    
    @bairroAdvogado.setter
    def bairroAdvogado(self, bairro: str) -> None:
        self.__bairroAdvogado = bairro

    #Métodos referentes ao atributo cepAdvogado
    @property
    def cepAdvogado(self) -> str:
        return self.__cepAdvogado

    @cepAdvogado.setter
    def cepAdvogado(self, cep: str) -> None:
        self.__cepAdvogado = cep
        
    #Métodos referentes ao atributo emailAdvogado
    @property
    def emailAdvogado(self) -> str:
        return self.__emailAdvogado

    @emailAdvogado.setter
    def emailAdvogado(self, email: str) -> None:
        self.__emailAdvogado = email

    def registrarAdvogado(self, self_a) -> None: # registrar um novo advogado ou alterar os dados de um advogado já cadastrado
        self._dados_Advogado.append(self_a)

    def consultaAdvogado(self, oab: int) -> str: # consultar um advogado específico 
        for advogado in self._dados_Advogado:
            if oab == advogado.__oabAdvogado:
                dict_Advogado = {
                "__oabAdvogado" : advogado.__oabAdvogado,
                "__nomeAdvogado" : advogado.__nomeAdvogado,
                "__enderecoAdvogado" : advogado.__enderecoAdvogado,
                "__telefoneAdvogado" : advogado.__telefoneAdvogado,
                "__bairroAdvogado" : advogado.__bairroAdvogado,
                "__cepAdvogado" : advogado.__cepAdvogado,
                "__emailAdvogado" : advogado.__emailAdvogado
                }
                return dict_Advogado # advogado.__dict__

    def listarAdvogado(self) -> None: # listar todos os advogados registrados
        for advogado in self._dados_Advogado:
            dict_Advogado = {
                "__oabAdvogado" : advogado.__oabAdvogado,
                "__nomeAdvogado" : advogado.__nomeAdvogado,
                "__enderecoAdvogado" : advogado.__enderecoAdvogado,
                "__telefoneAdvogado" : advogado.__telefoneAdvogado,
                "__bairroAdvogado" : advogado.__bairroAdvogado,
                "__cepAdvogado" : advogado.__cepAdvogado,
                "__emailAdvogado" : advogado.__emailAdvogado
                }
            print(json.dumps(dict_Advogado, sort_keys=False, indent=4))