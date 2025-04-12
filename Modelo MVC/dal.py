from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open ('pessoa.txt','w') as arq:
            arq.write(pessoa.nome + " "+ str(pessoa.idade) + " "+ pessoa.cpf)
    @classmethod
    def ler(cls):
        nome = 'Luis Fernando'
        idade = 33
        cpf = 1234567890
        return Pessoa(nome, idade,cpf)
    