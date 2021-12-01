def observed():
  observations = []
  for i in range(5):
    inp = input("Enter new value: ")
    observations.append(inp)
  return observations

def remove_observation(x = []):
  while True:
    print("Please enter an observation to be removed:")
    obs = input()
    if obs in x:
       x.remove(obs)
    print("Would you like to remove an observation?")
    response = input()
    if response.lower() != "yes":
      break

def run():
  lista = observed()
  remove_observation(lista)
  obs_set = set()
  for i in lista:
    tuplex = (i, lista.count(i))
    obs_set.add(tuplex)
  print("Observation:")
  for thing in obs_set:
    print(f"{thing[0]} has been observed {thing[1]} times")

run()
