n1 = int(input("Salve giovane passante, metti alla prova i miei numeri. Dimmene uno "))
n2 = int(input("Gran bel numero. Perché la mia magia sia valida me ne serve un altro però "))
sum = n1 + n2
print("La somma di " + str(n1) + " e " + str(n2) + " è " + str(sum))
n3 = int(input("Guarda che altra magia so fare; dimmi un altro numero ancora "))
n4 = int(input("Ancora uno dai "))
dif = n3 - n4
print("La differenza di " + str(n3) + " e " +str(n4) + " è "+ str(dif))
average = ( n1 + n2 + n3 + n4 )/ 4
print("E adesso osserva. La media di " + str(n1) + " "+ str(n2) + " " + str(n3) + " " + str(n4) + " è " + str(average))
if n1>n2 and n1>n3 and n1>n4:
  print("Il numero massimo è "  + str(n1))
if n2>n1 and n2>n3 and n2>n4:
  print("Il numero massimo è " + str(n2))
if n3>n1 and n3>n2 and n3>n4:
  print("Il numero massimo è " + str(n3))
if n4>n1 and n4>n2 and n4>n3:
  print("Il numero massimo è " + str(n4))
if n1<n2 and n1<n3 and n1<n4:
  print("Il numero minimo è " + str(n1))
if n2<n1 and n2<n3 and n2<n4:
  print("Il numero minimo è " + str(n2))
if n3<n1 and n3<n2 and n3<n4:
  print("Il numero minimo è " + str(n3))
if n4<n1 and n4<n2 and n4<n3:
  print("Il numero minimo è " + str(n4))

# soluzione alternativa di Claudio
max = n1
if n2 > max:
  max = n2

if n3 > max:
  max = n3

if n4 > max:
  max = n4

print(max)
