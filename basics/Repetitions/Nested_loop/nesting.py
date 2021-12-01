print("Please enter a sequence: ")
seq = input()
print("Please enter the character for marker: ")
marker = input()

m1 = 9999
m2 = 9999

for pos in range(len(seq)):
  let = seq[pos]
  if let == marker:
    if m1 == 9999:
      m1 = pos
    elif m2 == 9999:
      m2 = pos

print(f"The distance between two markers is {m2-m1-1}")