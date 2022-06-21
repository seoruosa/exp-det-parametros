from re import compile, split
from backpackInstance import BackpackInstance

def read_backpack_instances(filepath):
  """Following structure of https://www.vipinajayakumar.com/parsing-text-with-python/"""

  regex_dict = {
    'name': compile(r'(?P<name>knapPI[a-zA-Z\d_]+)\n'),
    'number_items': compile(r'n\s+(?P<number_items>\d+)\n'),
    'capacity': compile(r'c\s+(?P<capacity>\d+)\n'),
    'solution_profit': compile(r'z\s+(?P<profit>\d+)\n'),
    'time': compile(r'time\s+(?P<time>\d+\.\d+)\s*\n'),
    'array': compile(r'(?P<array>(( *\d+,{0,1})+))\n'),
    'end': compile(r'(?P<end>(\-*))\n')
  }

  def _parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex
    """

    for key, rx in regex_dict.items():
      match = rx.search(line)
      if match:
        return key, match
      # if there are no matches
    return None, None

  def _parse_array(arrayTxt, sepPattern = compile(r'\s*,\s*')):
    array = split(sepPattern, arrayTxt)
    p = int(array[1])
    w = int(array[2])
    sol = int(array[3])

    return (p, w, sol)

  with open(filepath) as f:
    lines = f.readlines()

  addedInstance = False

  instances = []

  profit = []
  weight = []
  solution = []

  for i, line in enumerate(lines):
    key, match = _parse_line(line)
    
    if key == 'name':
      name = match.group('name')
    elif key == 'number_items':
      n = int(match.group('number_items'))
    elif key == 'capacity':
      capacity = int(match.group('capacity'))
      instance = BackpackInstance(name, n, capacity)
      addedInstance = False

    elif key =='solution_profit':
      instance.setProfitSolution(match.group('profit'))
    elif key == 'time':
      # print(float(match.group('time')))
      pass
    elif key == 'array':
      p, w, sol = _parse_array(match.group('array'))
      
      profit.append(p)
      weight.append(w)
      solution.append(sol)

    elif key == 'end':
      if not(addedInstance):
        instance.setProfit(profit)
        instance.setWeight(weight)
        instance.setSolution(solution)

        profit = []
        weight = []
        solution = []

        instances.append(instance)
        addedInstance = True
    else:
      raise Exception(f"It was not possible to parse this line >>> {line}")
  
  return instances

def read_backpack_instance(filepath):
  """Following structure of https://www.vipinajayakumar.com/parsing-text-with-python/"""

  regex_dict = {
    'name': compile(r'(?P<name>knapPI[a-zA-Z\d_]+)\n'),
    'number_items': compile(r'n\s+(?P<number_items>\d+)\n'),
    'capacity': compile(r'c\s+(?P<capacity>\d+)\n'),
    'solution_profit': compile(r'z\s+(?P<profit>\d+)\n'),
    'array': compile(r'(?P<array>(( *\d+,{0,1})+))\n'),
  }

  def _parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex
    """

    for key, rx in regex_dict.items():
      match = rx.search(line)
      if match:
        return key, match
      # if there are no matches
    return None, None

  def _parse_array(arrayTxt, sepPattern = compile(r'\s*,\s*')):
    array = split(sepPattern, arrayTxt)
    p = int(array[0])
    w = int(array[1])

    return (p, w)

  with open(filepath) as f:
    lines = f.readlines()

  profit = []
  weight = []

  for i, line in enumerate(lines):
    key, match = _parse_line(line)
    
    if key == 'name':
      name = match.group('name')
    elif key == 'number_items':
      n = int(match.group('number_items'))
    elif key == 'capacity':
      capacity = int(match.group('capacity'))
      instance = BackpackInstance(name, n, capacity)

    elif key =='solution_profit':
      instance.setProfitSolution(match.group('profit'))

    elif key == 'array':
      p, w = _parse_array(match.group('array'))
      
      profit.append(p)
      weight.append(w)
    else:
      raise Exception(f"It was not possible to parse this line >>> {line}")
  
  instance.setProfit(profit)
  instance.setWeight(weight)
  
  return instance