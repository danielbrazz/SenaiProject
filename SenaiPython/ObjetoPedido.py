#ObjetoPedido
listaP = [] #lista global
 
class Pedido:   #OBJETO
    def __init__(self, name, qtd):
        #self.user = user
        self.nome = name   #nome item
        self.qtd = qtd     #quantidade
        self.aprovGen = 2  #gerente
        self.aprovCom = 2   #compras
        self.log = 2       #logistica
        self.entrega = 0   #entregue
        self.justificativa = 0 #caso negado
