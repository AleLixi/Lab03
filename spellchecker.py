import time
import dictionary as d
import multiDictionary as md
print("Dictionary.loadDictionary definito in:", d.Dictionary.loadDictionary.__code__.co_filename)
class SpellChecker:

    def __init__(self):
        pass

    def replaceChars(self, text):
        chars = "\\'*_-[]{}()<>?/|!@#$%^&*+=,."
        for c in chars:
            text = text.replace(c, '')
        return text

    def handleSentence(self, txtIn, language):
        start_time= time.perf_counter()
        dizionario= d.Dictionary()
        errori= []
        """else:
            md.MultiDictionary().searchWord(txtIn, language)"""
        if language == "italian":
            dizionario.loadDictionary("C:/Users/User/PycharmProjects/Lab03/resources/Italian.txt")
        if language == "english":
            dizionario.loadDictionary("C:/Users/User/PycharmProjects/Lab03/resources/English.txt")
        if language == "spanish":
            dizionario.loadDictionary("C:/Users/User/PycharmProjects/Lab03/resources/Spanish.txt")

        txtInPulito = self.replaceChars(txtIn)
        words = txtInPulito.split()
        for word in words:
            if word not in dizionario.dict:
                errori.append(word)
        if errori:
            print("using contains ")
            for err in errori:
                print(f"{err} ")
            end_time = time.perf_counter()
            execution_time= end_time - start_time
            print(f"Tempo di esecuzione: {execution_time:.4f} secondi")




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


