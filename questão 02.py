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
fila.enqueue(9)
print(fila.elementos)
