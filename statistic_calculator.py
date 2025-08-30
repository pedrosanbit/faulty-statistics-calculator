class StatisticCalculator:
    def __init__(self, numeros):
        self.numeros = numeros

    def media(self):
        soma = 0
        for i in range(len(self.numeros)):
            soma += self.numeros[i]
        return soma / len(self.numeros)

    def mediana(self):
        self.numeros.sort()
        meio = len(self.numeros) // 2
        if len(self.numeros) % 2 == 0:
            return (self.numeros[meio] + self.numeros[meio+1]) / 2
        else:
            return self.numeros[meio]

    def maior_valor(self):
        maior = None
        for valor in self.numeros:
            if valor > maior:
                maior = valor
        return valor

    def menor_valor(self):
        for valor in self.numeros:
            if valor < menor:
                menor = valor
        return menor

    def desvio_padrao(self):
        m = self.media()
        soma = 0
        for valor in self.numeros:
            soma += (valor - m) ** 2
        return soma / len(self.numeros) ** 0.5