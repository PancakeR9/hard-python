incipit = "Benvenuti al Moguri Casinò!"

print(incipit)

nome = input("Qual è il tuo nome, Kupò? ")

if len(nome) > 1:
    print("Ben arrivato "+ nome + " Kupò! ")

    cognome = input("Come sono conosciuti i tuoi avi nel regno? ")

    if len(cognome)>1:
        print(nome + " " + cognome + "?")
        print("Grande famiglia i " + cognome + ". Rendigli onore")
        
        eta = input("Ci siamo quasi, Kupò! Devo solo assicurarmi che tu sia abbastanza grande da poter camminare. Quanti anni hai, Kupò? ")
        
        if len(eta)>1 and int(eta) >= 18:
            print("Sembra proprio che dovrò lasciarti entrare, Kupò")
        else:
    
            print("Mi dispiace, Kupò")
            print("Non accettiamo bambini, ti aspetto tra qualche anno, Kupò! Cresci e diventa forte.")

    else:
        print("Non posso farti entrare senza sapere a chi riportare le tue spoglie, Kupò")

else:
    print("Se non mi dici il tuo nome non entrerà mai nella storia, Kupò")