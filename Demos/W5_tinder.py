def interests():
  print("Enter your interests one after the other, and enter \"stop\" when finished ")
  s1 = set()
  while True:
    activity = input()
    if activity == "stop":
      break
    s1.add(activity)
  return s1

def tinderDaSecond():
  print("First person: ")
  p1 = interests()
  print("Second person: ")
  p2 = interests()
  common = p1.intersection(p2)
  if len(common) >= 3:
    print(f"Yey - you are a match made in heaven! You have {len(common)} interests in common. ")
  else:
    print(f"Well, I don't think it will work out :( You only have {len(common)} interests in common")
    
tinderDaSecond()
