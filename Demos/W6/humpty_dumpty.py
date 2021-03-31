song = '''

Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
All the king's horses and all the king's men
Couldn't put, Humpty "together" again
Humpty "Dumpty" sat on a wall
Humpty Dumpty, had a great fall
All the king's horses and all the king's men
Couldn't put Humpty together again
Humpty Dumpty sat, on a wall
Humpty Dumpty had a great fall
All the king's horses and "all" the king's men
Couldn't put Humpty together again 

'''
lista =song.lower().replace("\"", "").replace("\'","").replace(",","").split()

#print(set(lista))

word_dict={}

for word in lista:
  if word in word_dict:
    word_dict[word] +=1
  else :
    word_dict[word] = 1


print(word_dict)