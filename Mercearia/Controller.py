from Models import Categoria, Estoque, Produtos, Pessoa,Funcionario,Venda
from Dao import DaoCategoria, DaoVenda,DaoEstoque, DaoFornecedor,DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A Categoria que deseja cadastrar ja existe')

    def removerCategoria(self,categriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categriaRemover, x))

        if len(cat) <=0:
            print('A categoria que deseja remover nao existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w')as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
    def aletrarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat)> 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1)==0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterada)else(x),x))
                print("A alteração foi efetuada com sucesso")
                #TODO: ALTERAR A CATEGORIA TAMBEM DO ESTOQUE
            else:
                print("A categiria para qual deseja alterar ja existe")
        else:
            print("A categoria que deseja alterar nao existe")

        with open('categoria.txt', 'w')as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
    def mostrarCategoria(self):
        categoria = DaoCategoria.ler()
        if len(categoria)==0:
            print("Categoria Vazia!")
        else:
            for i in categoria:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarPRoduto(self, nome, preço, categoria, quanridade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome ==nome, x))

        if len(h)> 0:
            if len(est) == 0:
                produto = Produtos(nome, preço,categoria)
                DaoEstoque.salvar(produto, quanridade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto ja existe em estoque')
        else:
            print('Categoria Inexistente')
    
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto removido com sucesso')
        else:
            print('O produto que deseja remover nao existe')
        
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome+"|"+ i.produto.preco+"|"+i.produto.categoria+"|"+str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self,nomeAlterar, novoNome,novoPreco,novaCategoria,novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(novoNome,novoPreco, novaCategoria),novaQuantidade)if(x.produto.nome == nomeAlterar)else(x),x)
                    print('PRoduto alterado com sucesso')
                else:
                    print('Produto ja cadastrado')
            else:
                print('O produto que deseja alterar nao existe')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome+"|"+ i.produto.preco+"|"+i.produto.categoria+"|"+str(i.quantidade))
                    arq.writelines('\n')
        else:
            print('A categoria informada nao existe')
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque Vazio')
        else:
            print('========== Produtos ==========')
            for i in estoque:
                
                print(f"Nome: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}\n"
                      )
                print("-------------------------------")

class ControllerVenda:
    def cadastrarVenda(self,nomeProduto, vendedor,comprador,quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        for i in x:
                if existe == False:
                    if i.produto.nome == nomeProduto:
                        existe = True
                        if i.quantidade >= quantidadeVendida:
                            quantidade = True
                            i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                            vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                            valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                            DaoVenda.salvar(vendido)

                temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write("")


        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

        if existe == False:
            print('O produto nao exite')
            return None
        elif not quantidade:
            print('A quantidade vendida não contem em estoque')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra


