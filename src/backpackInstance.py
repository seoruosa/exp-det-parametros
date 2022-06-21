# -*- coding: utf-8 -*-
"""backpackInstance.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1863nS31hygtDnvoKMeMZcmNE8SMEQToA
"""

class BackpackInstance:
  def __init__(self, name, n, capacity):
    self.name = name
    self.n = n
    self.capacity = capacity
    self.haveInstanceSolution = False
  
  def __repr__(self):
    return f"{self.__class__.__name__}({self.name}, n={self.n}, capacity={self.capacity})"
        
  def setProfitSolution(self, profitSolution):
    self.profitSolution = int(profitSolution)
  
  def getProfitSolution(self):
    return self.profitSolution

  def setProfit(self, profit):
    self.profit = self.__validate_array_size(profit, self.n)
  
  def getProfit(self):
    return self.profit

  def setWeight(self, weight):
    self.weight = self.__validate_array_size(weight, self.n)
  
  def getWeight(self):
    return self.weight
  
  def setSolution(self, solution):
    self.solution = self.__validate_array_size(solution, self.n)
    self.haveInstanceSolution = True
  
  def getSolution(self):
    return self.solution
  
  def validateSolution(self, newSolution):
    """Return True if new solution have the same profit of instance solution"""
    if not(self.haveInstanceSolution):
      return None
    else:
      pass
  

  def __validate_array_size(self, array, size):
    if len(array) == size:
      return array
    raise Exception("The input array has a number of elements different from size")