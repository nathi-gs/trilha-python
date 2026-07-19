class Progressao:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r
    
    def gerar_termos(self):
        termos = []

        for i in range(self.n):
            termo = self.a1 + i * self.r
            termos.append(termo)
        return termos
    
    def calcular_soma(self):
        an = self.a1 + (self.n - 1) * self.r
        soma = self.n * (self.a1 + an) / 2
        return soma

    