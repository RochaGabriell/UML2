from abc import abstractmethod
import json

class Pessoa:
    def __init__(self, nomePesssoa: str, enderecoPesssoa: str, bairroPesssoa: str, cidadePesssoa: str, cepPesssoa: int, ufPesssoa: str, telefonePesssoa: str, emailPesssoa: str) -> None:
        self._nomePesssoa = nomePesssoa
        self._enderecoPesssoa = enderecoPesssoa
        self._bairroPesssoa = bairroPesssoa
        self._cidadePesssoa = cidadePesssoa
        self._cepPesssoa = cepPesssoa
        self._ufPesssoa = ufPesssoa
        self._telefonePesssoa = telefonePesssoa
        self._emailPesssoa = emailPesssoa
        self._dados_Pesssoas = []

    #Métodos referentes ao atributo nomePessoa
    @property
    def nomePesssoa(self) -> str:
        return self._nomePesssoa

    @nomePesssoa.setter
    def nomePesssoa(self, nome: str) -> None:
        self._nomePesssoa = nome

    #Métodos referentes ao atributo enderecoPessso
    @property
    def enderecoPesssoa(self) -> str:
        return self._enderecoPesssoa
    
    @enderecoPesssoa.setter
    def enderecoPesssoa(self, endereco: str) -> None:
        self._enderecoPesssoa = endereco

    #Métodos referentes ao atributo bairroPesssoa
    @property
    def bairroPesssoa(self) -> str:
        return self._bairroPesssoa
    
    @bairroPesssoa.setter
    def bairroPesssoa(self, bairro: str) -> None:
        self._bairroPesssoa = bairro

    #Métodos referentes ao atributo cidadePesssoa
    @property
    def cidadePesssoa(self) -> str:
        return self._cidadePesssoa

    @cidadePesssoa.setter
    def cidadePesssoa(self, cidade: str) -> None:
        self._cidadePesssoa = cidade

    #Métodos referentes ao atributo cepPesssoa
    @property
    def cepPesssoa(self) -> int:
        return self._cepPesssoa

    @cepPesssoa.setter
    def cepPesssoa(self, cep: int) -> None:
        self._cepPesssoa = cep
    
    #Métodos referentes ao atributo ufPesssoa
    @property
    def ufPesssoa(self) -> str:
        return self._ufPesssoa
    
    @ufPesssoa.setter
    def ufPesssoa(self, uf: str) -> None:
        self._ufPesssoa = uf

    #Métodos referentes ao atributo telefonePesssoa
    @property
    def telefonePesssoa(self) -> str:
        return self._telefonePesssoa

    @telefonePesssoa.setter
    def telefonePesssoa(self, telefone: str) -> None:
        self._telefonePesssoa = telefone

    #Métodos referentes ao atributo emailPesssoa
    @property
    def emailPesssoa(self) -> str:
        return self._emailPesssoa

    @emailPesssoa.setter
    def emailPesssoa(self, email: str) -> None:
        self._emailPesssoa = email
    
    @abstractmethod
    def listarPessoa(self) -> str:
        pass

class PessoaFisica(Pessoa):
    def __init__(self, nomePesssoa: str, enderecoPesssoa: str, bairroPesssoa: str, cidadePesssoa: str, cepPesssoa: int, ufPesssoa: str, telefonePesssoa: str, emailPesssoa: str, cpfPessoa: str, rgPessoa: str) -> None:
        super().__init__(nomePesssoa, enderecoPesssoa, bairroPesssoa, cidadePesssoa, cepPesssoa, ufPesssoa, telefonePesssoa, emailPesssoa)
        self.__cpfPessoa = cpfPessoa
        self.__rgPessoa = rgPessoa

    #Métodos referentes ao atributo cpfPessoa
    @property
    def cpfPessoa(self) -> str:
        return self.__cpfPessoa

    @cpfPessoa.setter
    def cpfPessoa(self, cpf: str) -> None:
        self.__cpfPessoa = cpf

    #Métodos referentes ao atributo rgPessoa
    @property
    def rgPessoa(self) -> str:
        return self.__rgPessoa

    @rgPessoa.setter
    def rgPessoa(self, rg: str) -> None:
        self.__rgPessoa = rg

    def registrarPessoa(self, self_p) -> None:
        self._dados_Pesssoas.append(self_p)

    def consultarPessoa(self, cpf) -> str:
        for pessoa in self._dados_Pesssoas:
            if cpf == pessoa.__cpfPessoa:
                dict_Pessoa_Fisica = {
                    "_nomePesssoa": pessoa._nomePesssoa,
                    "_PessoaFisica__cpfPessoa": pessoa.__cpfPessoa
                }
                return dict_Pessoa_Fisica
    
    def listarPessoa(self) -> str:
        for pessoa in self._dados_Pesssoas:
            dict_Pessoa_Fisica = {
                "_nomePesssoa": pessoa._nomePesssoa,
                "_enderecoPesssoa": pessoa._enderecoPesssoa,
                "_bairroPesssoa": pessoa._bairroPesssoa,
                "_cidadePesssoa": pessoa._cidadePesssoa,
                "_cepPesssoa": pessoa._cepPesssoa,
                "_ufPesssoa": pessoa._ufPesssoa,
                "_telefonePesssoa": pessoa._telefonePesssoa,
                "_emailPesssoa": pessoa._emailPesssoa,
                "_PessoaFisica__cpfPessoa": pessoa.__cpfPessoa,
                "_PessoaFisica__rgPessoa": pessoa.__rgPessoa
                }
            print(json.dumps(dict_Pessoa_Fisica, sort_keys=False, indent=4))

class PessoaJuridica(Pessoa):
    def __init__(self, nomePesssoa: str, enderecoPesssoa: str, bairroPesssoa: str, cidadePesssoa: str, cepPesssoa: int, ufPesssoa: str, telefonePesssoa: str, emailPesssoa: str, cnpjPessoa: int) -> None:
        super().__init__(nomePesssoa, enderecoPesssoa, bairroPesssoa, cidadePesssoa, cepPesssoa, ufPesssoa, telefonePesssoa, emailPesssoa)
        self.__cnpjPessoa = cnpjPessoa

    #Métodos referentes ao atributo cnpjPessoa
    @property
    def cnpjPessoa(self) -> str:
        return self.__cnpjPessoa

    @cnpjPessoa.setter
    def cnpjPessoa(self, cnpj: str) -> None:
        self.__cnpjPessoa = cnpj

    def registrarPessoa(self, self_p) -> None:
        self._dados_Pesssoas.append(self_p)

    def consultarPessoa(self, cnpj) -> str:
        for pessoa in self._dados_Pesssoas:
            if cnpj == pessoa.__cnpjPessoa:
                dict_Pessoa_Juridica = {
                    "_nomePesssoa": pessoa._nomePesssoa,
                    "_PessoaJuridica__cnpjPessoa": pessoa.__cnpjPessoa
                }
                return dict_Pessoa_Juridica
                
    def listarPessoa(self) -> str:
        for pessoa in self._dados_Pesssoas:
            dict_Pessoa_Juridica = {
                "_nomePesssoa": pessoa._nomePesssoa,
                "_enderecoPesssoa": pessoa._enderecoPesssoa,
                "_bairroPesssoa": pessoa._bairroPesssoa,
                "_cidadePesssoa": pessoa._cidadePesssoa,
                "_cepPesssoa": pessoa._cepPesssoa,
                "_ufPesssoa": pessoa._ufPesssoa,
                "_telefonePesssoa": pessoa._telefonePesssoa,
                "_emailPesssoa": pessoa._emailPesssoa,
                "_PessoaJuridica__cnpjPessoa": pessoa.__cnpjPessoa
                }
            print(json.dumps(dict_Pessoa_Juridica, sort_keys=False, indent=4))