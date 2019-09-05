present = 307357870#Fólk á jörðinni núna
added = 2980325.274725274 #Fólk sem bætist við á hverju ári sem við reiknuðum út miðað við 365 daga(+fæðingar+innflytjendur og -dauði á ári)
year = int(input('Years:'))#Slærð inn árafjölda
if year < 0:#Má ekki vera mínustala
  print(' Invalid input!')
else:# Útkoma ef talan er plústala
    result = int((year* added) + present)
    print(' New population after ',end=''), 
    print( year,end=''), 
    print( ' years is ',end=''), 
    print( result)# Allt prentast í sömu línu
    