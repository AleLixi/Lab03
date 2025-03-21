import time
import dictionary as d
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def replaceChars(self, text):
        chars = "\\'*_-[]{}()<>?/|!@#$%^&*+=,."
        for c in chars:
            text = text.replace(c, '')
        return text

    def handleSentence(self, txtIn, language):
        dizionario= d.Dictionary
        errori= []
        if language == "italian":
            dizionario.loadDictionary("C:/Users/User/PycharmProjects/Lab03/resources/Italian.txt")
        if language == "english":
            dizionario.loadDictionary("C:/Users/User/PycharmProjects/Lab03/resources/English.txt")
        if language == "spanish":
            dizionario.loadDictionary("C:/User/User/PycharmProjects/Lab03/resources/Spanish.txt")

        txtInPulito = self.replaceChars(txtIn)
        words = txtInPulito.split()
        for word in words:
            if word not in dizionario:
                errori.append(word)
        return errori




    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


