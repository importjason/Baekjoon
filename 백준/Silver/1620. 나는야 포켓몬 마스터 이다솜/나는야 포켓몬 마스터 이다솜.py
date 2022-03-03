from sys import stdin,stdout

a,b = map(int, input().split())

pokedex = {}
for i in range(1, a+1) :
  pokemon = stdin.readline().rstrip()
  pokedex[i] = pokemon
  pokedex[pokemon] = i

for _ in range(b) :
  question = stdin.readline().rstrip()
  if question.isdigit() :
    stdout.write(pokedex[int(question)]+'\n')
  else :
    stdout.write(str(pokedex[question])+'\n')