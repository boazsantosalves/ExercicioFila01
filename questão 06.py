class Fila:
  def __init__(self):
    self.elementos = []

  def lenght(self):
    return len(self.elementos)

  def isEmpyt(self):
    return len(self.elementos)==0

  def enqueue(self,valor):
    self.elementos.append(valor)

  def dequeue(self):
    if(not(self.isEmpyt())):
      self.elementos.pop(0)

fila = Fila()
a = input("Digite o modelo e o ano do avião (separados por um espaço). Exemplo: f-5 2018\n")
fila.enqueue(a)
b = input("Digite o modelo e o ano do avião (separado por um espaço)\n")
fila.enqueue(b)
c = input("Digite o modelo e o ano do avião (separado por um espaço)\n")
fila.enqueue(c)
print("O primeiro avião está autorizado para a decolagem\n")
print(fila.elementos)
nAvioes = fila.lenght()
print("%d é o total de aviões na fila\n"%(nAvioes))
print("Características do primeiro avião:", fila.elementos[0])
