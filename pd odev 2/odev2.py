
import re

class Parser:
    def __init__(self, metin):
        self.tokens = re.findall(
            r'\d+(?:\.\d+)?|[a-zA-Z_]\w*|\S', metin
        )
        self.i = 0

    def bak(self):
        if self.i < len(self.tokens):
            return self.tokens[self.i]
        return None

    def al(self):
        token = self.bak()
        self.i += 1
        return token

    def ifade(self):
        sol = self.terim()
        while self.bak() in ('+', '-'):
            op = self.al()
            sol = (op, sol, self.terim())
        return sol

    def terim(self):
        sol = self.faktor()
        while self.bak() in ('*', '/'):
            op = self.al()
            sol = (op, sol, self.faktor())
        return sol

    def faktor(self):
        token = self.bak()

        if token == '(':
            self.al()
            sonuc = self.ifade()
            if self.bak() != ')':
                raise ValueError("Parantez eksik")
            self.al()
            return sonuc

        if token and re.fullmatch(r'\d+(?:\.\d+)?', token):
            return ("SAYI", self.al())

        if token and re.fullmatch(r'[a-zA-Z_]\w*', token):
            return ("DEGISKEN", self.al())

        raise ValueError("Hatali ifade")

def agac_yaz(agac, bosluk=""):
    if isinstance(agac, tuple):
        print(bosluk + str(agac[0]))
        for dal in agac[1:]:
            agac_yaz(dal, bosluk + "    ")
    else:
        print(bosluk + str(agac))

metin = input("Aritmetik ifade giriniz: ")

try:
    parser = Parser(metin)
    agac = parser.ifade()

    if parser.bak() is not None:
        raise ValueError("Fazladan karakter var")

    print("GECERLI IFADE")
    print("Parse Tree:")
    agac_yaz(agac)

except ValueError:
    print("GECERSIZ IFADE")
