import time
import dictionary as d
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def replaceChars(self, text):
        chars = "\\'*_-[]{}()<>?/|!@#$%^&*+="
        for c in chars:
            text = text.replace(c, '')
        return text

    def handleSentence(self, txtIn, language):
        errori= []
        counter_errori = 0
        if language == "italiano":
            d.Dictionary().loadDictionary("C:/Users/User/PycharmProjects/Lab03/it_dictionary.txt")
            txtInPulito = self.replaceChars(txtIn)
            words = txtInPulito.split()
            for word in words:
                if word not in d.Dictionary().dict:
                    errori.append(word)
                    counter_errori += 1

            else:
                md.MultiDictionary().searchWord(txtIn, language)
        if language == "inglese":
            d.Dictionary().loadDictionary("C:/Users/User/PycharmProjects/Lab03/en_dictionary.txt")
        if language == "spagnolo":
            d.Dictionary().loadDictionary("C:/Users/User/PycharmProjects/Lab03/es_dictionary.txt")

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


def replaceChars(text):
    pass