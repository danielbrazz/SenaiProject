import ObjetoPedido
import os
clear = lambda: os.system('cls')
lista = ObjetoPedido.listaP

pp = ObjetoPedido.Pedido("papel","100")
pp.aprovGen =1
lista.append(pp)
gg = ObjetoPedido.Pedido("caneta","5")
gg.aprovGen = 1
lista.append(gg)

class Compras:
    def Main():
        clear()
        print("#######PERFIL Compras#######")
        print("1-Verificar/Modificar solicitações")
        print("5-Logout")
        r = input(": ")
        if int(r) == 1:
            Compras.Lista()
        elif int(r) == 5:
            return
        else:
            Compras.Main()

    def Lista():
        clear()
        h = 0
        for x in range(len(lista)): #para cada item na lista
            if int(lista[x].aprovGen) == 1 :
                print(str(x)+" "+"Item: "+lista[x].qtd+" "+lista[x].nome)
                if int(lista[x].aprovCom) == 2:
                    print("Aguardando verificação")
                elif int(lista[x].aprovCom) == 1:
                    print("Aprovado")
                else:
                    print("Negado")
                print("")
                h=h+1

        if h == 0 :
            print("Aguardando requisições") 
        else:
            y = input("Modificar item nº:")
            for x in range(len(lista)):
                if int(lista[x].aprovGen) == 1 :
                    if x == int(y):
                        print(lista[x].qtd + " " +lista[x].nome)
                        r = input("Aprovar(1)   Reprovar(0)")
                        lista[x].aprovCom = r       
                    

        x = input("")
        Compras.Main()
Compras.Main()