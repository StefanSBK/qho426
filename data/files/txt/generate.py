def search(name):
  print("Searching...")
  data = {}
  with open(name) as f:
    for line in f:
      if line.startswith("Section"):
        items = line.split(":")
        section = items[1].strip()
      elif section in data:
        data[section].append(line.strip())
      else:
        data[section] = [line.strip()]
  print("Done!")
  return data

def run ():
  d = search("data/files/txt/books.txt")
  with open("data/files/txt/generated.csv", "w") as potato:
    for s, l_b in d.items():
      for item in l_b:
        potato.write(f"{s}, {item}\n")

run()

