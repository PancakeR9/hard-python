

n1 = input("Metti alla prova i miei numeri. Dimmene uno")


if len(n1)>0:

    print("Gran bel numero")

    n2 = input("Scegline ancora un altro giovane passante")


    sum = int(n1) + int(n2)


    if len(n2)>0:
        print(sum)
        print(dif)
    else:
        print("non hai ancora scelto un secondo numero")
else:
    print("Come pensi di mettermi alla prova se non mi dai un numero?")
 

