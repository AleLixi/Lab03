import spellchecker

sc = spellchecker.SpellChecker()


def chiedi_opzione():
    while True:
        user_input = input("Inserisci un numero intero tra 1 e 4: ")
        # Controlla se l'input è composto solo da cifre
        if user_input.isdigit():
            numero = int(user_input)
            # Verifica che il numero sia nel range desiderato
            if 1 <= numero <= 4:
                return numero
        # Se il controllo fallisce, stampa un messaggio e ripeti la richiesta
        print("Input non valido. Riprova.")

while(True):
    sc.printMenu()

    txtIn = chiedi_opzione()




    if txtIn == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")


        continue

    if txtIn == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        continue

    if txtIn == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if txtIn == 4:
        break


