from Graph import Grafo
from estafeta import *
from transporte import *
from encomenda import *
from rua import *
from cliente import *
from Heu import Heu
from menu import *

""" Zé: Corrigir os algoritmos(Greedy) e testar os outros(BFS, DFS, A*)
        Implementar a decisão de transporte

    Marta: Melhorar AdicionarCliente e AdicionarEstafeta

""" 

def main():
    listEncomendas = list()

    # apagar!
    #listEstafetas = list()
    #e1 = Estafeta(1,"João Afonso",15,5)
    #e2 = Estafeta(2,"Maria Alberta",14,3)
    #e3 = Estafeta(3,"António Moura",19,7)
    #e4 = Estafeta(4,"Francisca Maria",21,5)
    #e5 = Estafeta(5,"José Oliveira",50,10)
    #e6 = Estafeta(6,"Gonçalo Machado",31,7)
    #e7 = Estafeta(7,"Maria João",100,50)
    #e8 = Estafeta(8,"Pedro Lopes",42,9)
    #e9 = Estafeta(9,"Marta Rodrigues",79,16)
    #listEstafetas.append(e1)
    #listEstafetas.append(e2)
    #listEstafetas.append(e3)
    #listEstafetas.append(e4)
    #listEstafetas.append(e5)
    #listEstafetas.append(e6)
    #listEstafetas.append(e7)
    #listEstafetas.append(e8)
    #listEstafetas.append(e9)


    heuristicas = Heu()
    heuristicas.fillHeuristicas() #mudar esta funcao


    t1 = Transporte("Bicicleta", 5, 10)
    t2 = Transporte("Mota", 20, 35)
    t3 = Transporte("Carro", 100, 50)

    rua0 = Rua("Central", "São Lázaro") #Central da Health Planet
    rua1 = Rua("Rua da Confeiteira", "Palmeira")
    rua2 = Rua("Rua de Redondo", "Adaufe")
    rua3 = Rua("Rua de São Martinho", "Dume")
    rua4 = Rua("Rua 5 de Outubro", "Real")
    rua5 = Rua("Rua da Universidade", "Gualtar")
    rua6 = Rua("Rua Santa Margarida", "São Vicente")
    rua7 = Rua("Rua de São José", "São Vitor")
    rua8 = Rua("Rua do Raio", "São Vitor")
    rua9 = Rua("Avenida Dom Joao II", "Nogueiró")
    rua10 = Rua("Rua do Fujacal", "São Lazaro")
    rua11 = Rua("Rua Joãozinho Azeredo", "Maximinos")
    rua12 = Rua("Rua da Igreja", "Nogueira")
    rua13 = Rua("Rua da Senra", "Lamacães")
    lista_ruas = [rua1,rua2,rua3,rua4,rua5,rua6,rua7,rua8,rua9,rua10,rua11,rua12,rua13]

    # apagar!
    #listClientes = list()
    #client1 = Cliente(1, "Ana Silva", rua3)
    #client2 = Cliente(2, "José Pereira", rua1)
    #client3 = Cliente(3, "Mariana Costa", rua5)
    #client4 = Cliente(4, "Rui Oliveira", rua9)
    #client5 = Cliente(5, "Carla Sousa", rua12)
    #client6 = Cliente(6, "Hugo Fernandes",rua6)
    #client7 = Cliente(7, "Beatriz Santos", rua7)
    #client8 = Cliente(8, "André Martins", rua10)
    #listClientes.append(client1)
    #listClientes.append(client2)
    #listClientes.append(client3)
    #listClientes.append(client4)
    #listClientes.append(client5)
    #listClientes.append(client6)
    #listClientes.append(client7)
    #listClientes.append(client8)


    g = Grafo(heuristicas)
    g.add_edge(rua0, rua3, 3.7)
    g.add_edge(rua0, rua4, 3.3)
    g.add_edge(rua0, rua5, 2.2)
    g.add_edge(rua0, rua6, 0.5)
    g.add_edge(rua0, rua8, 0.3)
    g.add_edge(rua0, rua9, 2.9)
    g.add_edge(rua0, rua10, 2.3)
    g.add_edge(rua0, rua11, 1.8)
    g.add_edge(rua0, rua13, 3.1)
    g.add_edge(rua1, rua3, 2.8) 
    g.add_edge(rua1, rua2, 2.8) 
    g.add_edge(rua1, rua4, 1.7) 
    g.add_edge(rua1, rua6, 3.6) 
    g.add_edge(rua2, rua5, 1.5) 
    g.add_edge(rua3, rua4, 1.2) 
    g.add_edge(rua3, rua6, 1.5) 
    g.add_edge(rua3, rua7, 3.0) 
    g.add_edge(rua4, rua6, 1.3) 
    g.add_edge(rua4, rua7, 2.0) 
    g.add_edge(rua4, rua11, 1.9)
    g.add_edge(rua5, rua7, 1.5) 
    g.add_edge(rua5, rua8, 1.7) 
    g.add_edge(rua5, rua9, 1.6) 
    g.add_edge(rua6, rua7, 1.0) 
    g.add_edge(rua6, rua8, 0.8)
    g.add_edge(rua6, rua10, 1.3)
    g.add_edge(rua6, rua11, 1.1)
    g.add_edge(rua7, rua8, 0.5)
    g.add_edge(rua7, rua9 , 1.2)
    g.add_edge(rua8, rua9 , 1.0)
    g.add_edge(rua7, rua12, 2.9) 
    g.add_edge(rua7, rua13, 3.5) 
    g.add_edge(rua8, rua10, 1.4) 
    g.add_edge(rua8, rua13, 2.7) 
    g.add_edge(rua9, rua12, 2.0) 
    g.add_edge(rua9, rua13, 2.9) 
    g.add_edge(rua10, rua11, 1.3) 
    g.add_edge(rua10, rua12, 1.9)
    g.add_edge(rua12, rua13, 0.9) 

    #leitura dos ficheiros txt com os estafetas e clientes
    carregarEstafetas('./estafetas.txt')
    carregarClientes('./clientes.txt', lista_ruas)

    m = Menu()
    print("\n******** BEM VINDO AO HEALTH PLANET ********\n")

    userInput = -1
    while userInput != 0:

        m.printMenu()
        userInput = int(input("Escolha opção: "))

        #Opçoes Cliente
        if userInput == 1: 
            opcao1 = -1
            while opcao1 != 0:
                m.menu_cliente()
                opcao1 = int(input("Escolha opção: "))
                #adicionar novo cliente - melhorar isto
                if opcao1 == 1: 
                    clienteNome = input("Escolha nome:")
                    
                    m.printRuas(lista_ruas)
                    clienteRua = int(input("Escolha Rua:"))

                    if 1 <= clienteRua < len(lista_ruas):
                        rua_escolhida = lista_ruas[clienteRua - 1]
                        print("Rua escolhida:", rua_escolhida)
                    
                        Cliente.adicionarCliente(clienteNome, rua_escolhida)
                        print("Cliente Criado.")
                
                    else:
                        print("Índice fora dos limites da lista. Escolha inválida.")

                #imprimir lista clientes - melhorar!
                if opcao1 == 2:
                    #print(listClientes)
                    print(Cliente.listaClientes)

        #Opcoes Estafeta
        if userInput == 2:
            opcao2 = -1
            while opcao2 != 0:
                m.menu_estafetas()
                opcao2 = int(input("Escolha opção: "))
                
                #adicionar novo estafeta
                if opcao2 == 1: 
                    estafetaNome = input("Escolha nome:")
                    Estafeta.adicionarEstafeta(estafetaNome,0,0)

                
                #imprimir lista estafetas -melhorar!
                if opcao2 == 2:
                    #print(listEstafetas)
                    print(Estafeta.listaEstafeta)


        if userInput == 3:
            encomendaIdC = int(input("Id Cliente: "))
            peso = float(input("Peso da Encomenda: "))
            volume = float(input("Volume da encomenda(em centímetros cúbicos): "))
            hora_limite = input("Hora limite de entrega(hh:mm): ")
            morada = rua1
            
            for cliente in Cliente.listaClientes:
                if cliente.getId() == encomendaIdC:
                    encomenda = Encomenda(0,encomendaIdC,peso,volume,hora_limite,cliente.getRua())
                    (path, custo, visitados) = g.procura_aStar(cliente.getRua(),morada)
                    print(path)
                    print(custo)
                    print(visitados)
                    break
            

                      
        #Imprimir Ruas
        if userInput == 5: 
            print(g.imprime_aresta()) #imprime arestas - trocar!

        #Desenhar Grafo
        if userInput == 6:
            g.desenha()
            
        #Guardar alterações
        if userInput == 7:
            guardarEstafetas('./estafetas.txt')
            guardarClientes('./clientes.txt')
            print("Alterações Guardadas!")


        #acrescentar aqui cenas...      
        if userInput == 0: #Sair
            print("\nA sair...")

        else:
            print("Input inválido.")


if __name__ == "__main__":
    main()