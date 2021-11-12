import requests
from .utils import getData


class Sozluk:

    def __init__(self, kelime):
        self.data = getData(kelime)
        self.kelime = kelime
        self.anlamlar = []
        self.deyimler = []
        self.ornekler = []
        self.parseData()

    # def __str__(self):

    #     return f"Anlam: {self.anlamlar[0]}\nOrnek: {self.ornekler[0]}\nAtasozu: {self.deyimler[0]}\nDaha fazla anlam ve ornek icin lutfen metodlari kullanin."

    def getAnlamlar(self):  # Anlamlar

        self.anlamlar = [anlam['anlam']
                         for anlam in self.data[0]['anlamlarListe']]

    def getDeyimler(self):  # Deyimler

        self.deyimler = [anlam['madde']
                         for anlam in self.data[0]['atasozu']]

    def getOrnekler(self):    # Ornekler
        self.ornekler = []
        for anlam in self.data[0]['anlamlarListe']:
            for ornek in anlam['orneklerListe']:
                self.ornekler.append(ornek['ornek'])

    def parseData(self):
        self.getAnlamlar()
        self.getDeyimler()
        self.getOrnekler()