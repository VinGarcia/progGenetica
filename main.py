import math
import random

class Individuo():
  
  Formula = None

  # Insere um novo galho
  def Mutacao1(self):
    node = self.Formula.ChooseRandomNode()

    chosen = [0,1][random.randint(0,1)]

    temp = node.filhos[chosen]
    node.filhos[chosen] = Arvore.CreateRandomNode()

    side = [0,1][random.randint(0,1)]

    node.filhos[chosen].filhos[side] = temp
    node.filhos[chosen].filhos[0 if side else 1] = Arvore.CreateRandomLeaf()

  
  # Remove um galho
  def Mutacao2(self):
    node = self.Formula.ChooseRandomNode()

    chosen = 1 if node.filhos[1].tipo == 'o' else 0

    node.valor = node.filhos[chosen].valor
    node.filhos = node.filhos[chosen].filhos

  # Muda um tipo de operador
  def Mutacao3(self):
    node = self.Formula.ChooseRandomNode()
    node.tipo = ['+', '-', '*'][random.randint(0, 2)]
    
  # Muda o valor de uma folha
  def Mutacao3(self):
    node = self.Formula.ChooseRandomNode()

    folhaNum = 0 if node.filhos[1].tipo == 'o' else 1
    folha = node.filhos[folhaNum]

    folha.tipo = ['c', 'v'][random.randint(0, 1)]
    if folha.tipo == 'c':
      folha.valor = random.random()*2000-1000
    if folha.tipo == 'v':
      folha.valor = ['x', 'y'][random.randint(0, 1)]

  def Crossover(self, Pai, Mae):
    firstNode = Pai.Formula
    secondNode = Mae.Formula

    if random.random() > 0.5:
      left = firstNode.filhos[0]
      right = secondNode.filhos[1]
    else:
      left = secondNode.filhos[0]
      right = firstNode.filhos[1]

    child = Individuo(False)
    child.Formula.valor = [Pai.valor, Mae.valor][random.randint(0,1)]
    child.Formula.filhos[0] = left.CopyTree()
    child.Formula.filhos[1] = right.CopyTree()

    return child
  
  def Fitness(self):
    pass
  
  def __init__(self, makeLeafs=True):
    self.Formula = Arvore.CreateRandomNode()

    if makeLeafs:
      self.Formula.filhos[1] = Arvore.CreateRandomLeaf()
      self.Formula.filhos[0] = Arvore.CreateRandomLeaf()

class Arvore():
  
  tipo = None
  valor = None
  
  filhos = [None, None]

  def __init__(self, tipo, valor):

    if type(tipo) != str:
      raise Exception("Type must be a string!")

    if tipo == 'o' and valor not in ['+','-','*']:
      raise Exception("The value of an operator must be one of '+', '-', '*'")

    if tipo == 'v' and valor not in ['x', 'y']:
      raise Exception("The value of a variable must be one of 'x', 'y'")

    if tipo == 'c':
      try:
        valor = float(valor)
      except:
        raise Exception("The value of a constant must be a number!")

    self.tipo = tipo
    self.valor = valor
    self.filhos = [None, None]
    
  def ChooseRandomNode(self):
    selected = None
    if random.random() > 0.5:
      selected = self.filhos[0]
    else:
      selected = self.filhos[1]
    if selected.tipo == 'o':
      return selected.ChooseRandomNode()
    else:
      return self

  # Tested
  def CopyTree(self):
    Copy = Arvore(self.tipo, self.valor)
    if self.tipo != 'o':
      return Copy
    else:
      if(self.filhos[0]):
        Copy.filhos[0] = self.filhos[0].CopyTree()
      if(self.filhos[1]):
        Copy.filhos[1] = self.filhos[1].CopyTree()
      return Copy

  # Tested
  def CreateRandomNode():
    valor = ['+', '-', '*'][random.randint(0, 2)]
    return Arvore('o', valor)

  # Tested
  def CreateRandomLeaf():
    tipo = ['c', 'v'][random.randint(0, 1)]
    if tipo == 'c':
      valor = random.random()*2000-1000
    if tipo == 'v':
      valor = ['x', 'y'][random.randint(0, 1)]

    return Arvore(tipo, valor)

  # Tested
  def __str__(self):
    return "Tipo: %s, Valor: %s" % (self.tipo, self.valor)

  def printAll(self):
    levels = self._printAll()

    for level in levels:
      resp = ''
      for item in level:
        resp += item
      print(resp)

  def _printAll(self, shared={'resp':[]}, level=0):

    shared['resp'][level].append(str(self))

    shared['seq']+=1
    self.filhos[0].printAll(shared, level+1)
    shared['seq']+=1
    self.filhos[1].printAll(shared, level+1)

    return shared



if __name__ == '__main__':
  # a = Arvore('c', 1000)
  # a = Arvore('c',-1000)
  # a = Arvore('v','x')
  # a = Arvore('o','+')

  # b = a.CopyTree()
  # print(a.tipo, a.valor)
  # print(b.tipo, b.valor)

  # a.filhos[0] = Arvore.CreateRandomNode()
  # filho = a.filhos[0]
  # print(filho.tipo, filho.valor, filho.filhos)
  # filho = None
  # filho = Arvore.CreateRandomNode()
  # filho.filhos[1] = Arvore.CreateRandomLeaf()
  # print(filho.tipo, filho.valor, filho.filhos[1])

  root = Arvore.CreateRandomNode()
  root.filhos[0] = Arvore.CreateRandomLeaf()
  root.filhos[1] = Arvore.CreateRandomLeaf()

  # root.filhos[0].filhos[0] = Arvore.CreateRandomLeaf()
  # root.filhos[0].filhos[1] = Arvore.CreateRandomLeaf()

  # root.filhos[1].filhos[0] = Arvore.CreateRandomLeaf()
  # root.filhos[1].filhos[1] = Arvore.CreateRandomLeaf()

  #print(root.ChooseRandomNode())

  ind = Individuo(False)
  ind.Formula = root

  root.printAll()
  ind.Mutacao1()
  root.printAll()













  
