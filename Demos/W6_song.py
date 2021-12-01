song = '''Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish
6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap,
One pound, one pound

Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Have, have a look, 1 pound fish
Have, have a look, 1 pound fish
Very very good, 1 pound fish
Very very cheap, 1 pound fish

Come on ladies, come on ladies
Come on ladies, come on ladies
Come on ladies, come on ladies, 1 pound fish
Come on ladies, come on ladies, 1 pound fish

Come on ladies, come on ladies, 1 pound fish

6 for £5, or £1 each
6 for £5, or £1 each
Very very good and very very cheap
One pound fish'''


l = song.lower().replace(",", "").split()
print(l)
print("-"*20)
song_set = set(l)
print(song_set)
print("-"*20)
print(len(song_set))
print("-"*20)
dicto = {}
for i in l:
  dicto[i] = dicto.get(i,0) + 1

print(dicto)

