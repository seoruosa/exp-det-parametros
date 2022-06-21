# from random import seed
import numpy as np

def SA(f, N, alfa, iter_max_temp, temp_ini, sol_ini, temp_end, sol_is_feasible):
  """Implementation of simulated annealing algorithm
  Based on http://www.decom.ufop.br/prof/marcone/Disciplinas/InteligenciaComputacional/InteligenciaComputacional.pdf page 21

  Parameters: 
  f (function):
  N (function):
  alfa (double):
  iter_max_temp (int):
  temp_ini (double): initial temperature
  sol_ini : initial solution
  temp_end (double): final temperature

  Returns:
  a solution
  
  """
  sol_best = sol_ini
  f_sol_best = f(sol_ini)

  sol_actual = sol_best
  f_sol_actual = f_sol_best

  iter_temp = 0
  temp = temp_ini

  while temp > temp_end:
    while iter_temp < iter_max_temp:
      iter_temp += 1

      neigh = N(sol_actual)
      x = neigh
      # print(f"{x} -> f: {f(x)} -> is {'' if sol_is_feasible(x) else 'not '}feasible")
      f_neigh = f(neigh)

      delta = f_neigh - f_sol_actual

      if delta < 0:
        sol_actual = neigh
        f_sol_actual = f_neigh

        if f_sol_actual < f_sol_best and sol_is_feasible(sol_actual):
          # found a best solution
          sol_best = sol_actual
          f_sol_best = f_sol_actual
          # print(f"Improve solution -> f_best: {f_sol_best}")
      else:
        x = np.random.random()
        if x < np.exp(-delta/temp):
          sol_actual = neigh
          f_sol_actual = f_neigh
    temp *= alfa
    iter_temp = 0
    # print(f"Changed temperature -> temp: {temp}")
  
  return sol_best