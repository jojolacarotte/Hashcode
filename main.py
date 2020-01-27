print('Hashcode : Exercice sur les parts de Pizza')
print('jojolacarotte algorithm\'s')

# ======= Input =======
#f = open("jdd/a_example.in", "r")
#f = open("jdd/b_small.in", "r")
#f = open("jdd/c_medium.in", "r")
f = open("jdd/d_quite_big.in", "r")
#f = open("jdd/e_also_big.in", "r")

maxSlices, NbTypesOfPizza = f.readline().split()
typeOfPizza = f.readline().split()

blabla = {}
index = 0
for a in typeOfPizza:
  blabla[index] = int(a)
  index = index + 1

showRule = False

if showRule:
  print(f'Données en entrée :\n')
  print(f'Max Slices : {maxSlices}')
  print(f'NbTypesOfPizza : {NbTypesOfPizza}')
  print(f'typeOfPizza : {typeOfPizza}')
  print(f'type with number type:{blabla}\n')

list = []
max = 0
currentBestNb = 0
argsRange = [(0, len(blabla)-1, 1),(len(blabla)-1, -1, -1)]
haveMax = False

for z in range(0,2,1):
  for x in range(argsRange[0][0], argsRange[0][1], argsRange[0][2]):
    obj = {}
    currentBestNb += blabla[x]
    obj[x] = blabla[x]
    for y in range(argsRange[1][0], argsRange[1][1], argsRange[1][2]):
      currentBestNb += blabla[y]
      if currentBestNb > int(maxSlices):
        currentBestNb = 0
        break
      else:
        obj[y] = blabla[y]

      if max < currentBestNb:
        list.clear()
        list.append((currentBestNb, obj))
        max = currentBestNb
      if max == int(maxSlices):
        haveMax = True
        break
    if haveMax:
      break
  argsRange.reverse()
      
print(f'Mon nombre de part max trouvé : {max}')
print(f'{int(maxSlices) - max} meurent de faim, désolé')
print(f'Avec ces types là : {list}')