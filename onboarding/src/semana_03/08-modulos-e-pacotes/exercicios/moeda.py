def aumentar(valor, taxa=0.1, formatar=False):
    if formatar ==  True:   
        return moeda(valor + (valor * taxa))
    else:
        return valor + (valor * taxa)
    
def diminuir(valor, taxa=0.1, formatar=False):
    if formatar == True:
        return moeda(valor - (valor * taxa))
    else:
        return valor - (valor * taxa)


def dobro(valor, formatar=False):
    if formatar == True:
        return moeda(valor * 2)
    else:
        return valor * 2

def metade(valor, formatar=False):
    if formatar == True:
        return moeda(valor / 2)
    return valor / 2

def moeda(valor):
    return f"R${valor:.2f}".replace('.', ',')