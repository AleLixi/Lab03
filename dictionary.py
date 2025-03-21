class Dictionary:
    def __init__(self):
        self._dict = set()

    def loadDictionary(self,path):
        try :
            with open(path, 'r', encoding='utf-8') as file:
                for line in file:
                    word = line.strip().lower
                    if word:
                        self._dict.add(word)
        except Exception as e:
            print("Errore nel caricamento del dizionario:", e)




    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict