# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}


#1 
print('------------------------------------------------------------')

def showObjectKeys(audi):
    myList = list(audi.values())
    print(myList)
    

showObjectKeys(audi)