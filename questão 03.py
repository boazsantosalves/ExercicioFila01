class Fila:
  def __init__(self):
    self.elementos = []

  def lenght(self):
    return len(self.elementos)

  def isEmpyt(self):
    return len(self.elementos)==0

  def enqueue(self,valor):
    if (self.lenght())<20:
      self.elementos.append(valor)
    else:
      print("A quantidade máxima de pacientes já foi atingida")

  def dequeue(self):
    if(not(self.isEmpyt())):
      self.elementos.pop(0)

fila = Fila()
for i in range(21):
  fila.enqueue(i)

print(fila.elementos)
