from controller import PessoaController

while True:
    desicao = int(input('Digite 1 para salvar um apessoa ou digite 2 para ver a pessoa e 3 para sair: '))
    if desicao == 3:
        break
    if desicao ==1:
        nome = input('Digite seu Nome: ')
        idade = int(input('Digite sua Idade: '))
        cpf = input('Digite seu CPF: ')
        if PessoaController.cadastrar(nome,idade,cpf):
            print('Usuario cadastrado com sucesso')
        else:
            print('Digite valores validos')