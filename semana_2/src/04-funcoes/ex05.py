""" Exercício 5 """
individuo = {
    'altura': 1.79,
    'peso': 78.5
}

def calculadora(individuo):
    imc = individuo['peso'] / (individuo['altura'] ** 2)
    return imc

imc = calculadora(individuo)

print(imc)

def obter_classificacao(imc):
    if imc < 18.5 : classificacao = 'Baixo peso'
    elif 18.5 <= imc <= 24.9 : classificacao = 'Peso normal'
    elif 25.0 <= imc <= 29.9 : classificacao = 'Excesso de peso'
    elif 30.0 <= imc <= 34.9 : classificacao = 'Obesidade de Classe 1'
    elif 35.0 <= imc <= 39.9 : classificacao = 'Obesidade de classe 2'
    else: classificacao = 'Obesidade de Classe 3'
    return classificacao
    
classificacao = obter_classificacao(imc)
print(classificacao)

def situacao_individuo(imc):
    if imc < 18.5 : situacao = 'Ganhar peso'
    elif 18.5 <= imc <= 24.9 : situacao = 'Normal'
    else: situacao = 'perder peso'
    return situacao

situacao = situacao_individuo(imc)
print(situacao)
