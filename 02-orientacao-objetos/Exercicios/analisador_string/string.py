class AnalisadorString:
    def __init__(self, palavra):
        self.palavra = palavra

    def numero_de_caracteres(self):
        return len(self.palavra)

    def em_maiusculo(self):
        return self.palavra.upper()
    
    def em_minusculo(self):
        return self.palavra.lower()
    
    def contar_vogais(self):
        vogais = "aeiouAEIOU"
        contador = 0
        
        for caracter in self.palavra:
            if caracter in vogais:
                contador += 1
        return contador
    
    def contem_ifb(self):
        return "IFB" in self.palavra.upper()