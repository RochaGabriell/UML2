# from models.Advogado import Advogado
# from models.Assume import Assume
from models.Processo import Processo
from models.Pessoa import Pessoa, PessoaFisica, PessoaJuridica
from models.Audiencia import Audiencia
from models.Custa import Custa
from models.Vara import Vara
# from models.Tribunal import Tribunal

def main():
    
    print("- MODULO PESSOA -") # Modulo Pessoa

    pessoa_fisica = PessoaFisica("Gabriel Rocha Paes da Costa", "Av. Adolfo Ferreira dos Santos", "Centro", "Anisio de Abreu", 64780000, "PI", "(89) 98127-4201", "gabrielrocha1902@gmail.com", "614.022.983-22", "234.234")
    pessoa_fisica1 = PessoaFisica("Alan Nascimento Honorio", "Av. Ferreira dos Sem Santos", "Centro", "Pernagua", 64540000, "PI", "(89) 42344-4202", "honotioalan@gmail.com", "634.342.983-13", "2341423-3")
    pessoa_fisica2 = PessoaFisica("Oscar Bin Laden", "Av. Sem nome", "Bairro", "Corrente", 64980000, "PI", "(89) 43212-5434", "binladenoscar@gmail.com", "432.234.983-00", "1243433")
    pessoa_fisica.registrarPessoa(pessoa_fisica)
    pessoa_fisica.registrarPessoa(pessoa_fisica1)
    pessoa_fisica.registrarPessoa(pessoa_fisica2)

    pessoa_juridica = PessoaJuridica("Felipe Ferreira dos Santos", "Av. Dom Pedro", "Centro", "Corrente", 64980000, "PI", "(89) 99932-2341", "fgsantosti@gmail.com", "68.698.199/0001-07")
    pessoa_juridica1 = PessoaJuridica("Dom Pedro IV da Silva", "Av. Dom Pedro I", "Centro", "Corrente", 64980000, "PI", "(89) 99932-2341", "pedrodmmdas.com", "43.423.5345/0001-34")
    pessoa_juridica2 = PessoaJuridica("Paulo Filho da Silva Junir", "Av. Pedro da Silva", "Centro", "Teresina", 64980000, "PI", "(89) 124234-3243", "dasdsadsadwf@gmail.com", "76.698.423/0001-23")
    pessoa_juridica.registrarPessoa(pessoa_juridica)
    pessoa_juridica.registrarPessoa(pessoa_juridica1)
    pessoa_juridica.registrarPessoa(pessoa_juridica2)

    pessoa_fisica.listarPessoa()
    pessoa_juridica.listarPessoa()



    print("- MODULO VARA -") # Modulo Vara

    vara = Vara()
    
    print("- MODULO PROCESSO -") # Modulo Processo

    busca_f = pessoa_fisica.consultarPessoa("634.342.983-13")
    busca_j = pessoa_juridica.consultarPessoa("43.423.5345/0001-34")

    processo = Processo("T24235R", "10/10/2022", "22/02/2023", "Processo Judicial de Desapropriacao", True, busca_f, 
    busca_j)

    busca_f = pessoa_fisica.consultarPessoa("432.234.983-00")
    busca_j = pessoa_juridica.consultarPessoa("68.698.199/0001-07")

    processo1 = Processo("TF2343", "25/10/2022", "15/07/2023", "Processo cautelar", False, busca_f, busca_j)
    # processo2 = Processo("TF344343", "31/10/2022", "20/01/2023", "Processo de Conhecimento Declaratorio", True, Pessoa, Pessoa)
    processo.registrarProcesso(processo)
    processo.registrarProcesso(processo1)
    #processo.registrarProcesso(processo2)

    processo.listarProcesso()





    print("- MODULO AUDIENCIA -") # Modulo Audiencia

    b = processo.consultarProcesso("T24235R")

    audiencia = Audiencia("23/10/2022", "Audiencia de Conciliacao ou Mediacao", b)
    audiencia1 = Audiencia("30/11/2023", "Tutela de Urgencia", b)

    b = processo.consultarProcesso("TF2343")

    audiencia2 = Audiencia("19/10/2022", "Audiencia de justificacao", b)
    audiencia3 = Audiencia("01/12/2022", "Audiencia de instrucao e julgamento.", b)

    audiencia.registrarAudiencia(audiencia)
    audiencia.registrarAudiencia(audiencia1)
    audiencia.registrarAudiencia(audiencia2)
    audiencia.registrarAudiencia(audiencia3)

    audiencia.listarAudiencia()

    # audiencia.consultarAudiencia("T24235R")



    

    print("- MODULO CUSTA -") # Modulo Custa

    b = processo.consultarProcesso("T24235R")

    custa = Custa("10/10/2022", "Interposicao", 1333.38, b)
    custa1 = Custa("10/11/2022", "Elaboracao de Memoriais", 1333.38, b)

    b = processo.consultarProcesso("TF2343")

    custa2 = Custa("25/01/2022", "Sustentacao Oral", 5333.49, b)
    custa3 = Custa("30/02/2022", "contra-razoes", 1333.38, b)

    custa.registarCusta(custa)
    custa.registarCusta(custa1)
    custa.registarCusta(custa2)
    custa.registarCusta(custa3)

    custa.listarCusta()
    # print(custa.consultarCusta("Sustentacao Oral"))   


if __name__ == "__main__":
    main()