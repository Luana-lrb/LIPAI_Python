""" Exercício 6 """
aquario = {
    'comprimento': 23.5,
    'altura': 15.79,
    'largura': 8.5
}
def volume(aquario):
    vol = (aquario['comprimento'] * aquario['altura'] * aquario['largura'] ) / 1000
    return vol

vol = volume(aquario)
print(vol)

def potencia_termostato(temp_desejada, temp_ambiente, volume):
    potencia = volume * 0.05 * (temp_desejada - temp_ambiente)
    return potencia

pot = potencia_termostato(35.7, 30.4, vol)
print(pot)

def filtragem(volume):
    filtro_min = 2 * volume
    filtro_max = 3 * volume
    return filtro_min, filtro_max

filtro = filtragem(vol)
print(filtro)
