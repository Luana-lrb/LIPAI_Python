""" Exercício 3"""

meses = {
        1: "Janeiro",
        2: "Fevereiro", 
        3: "Março", 
        4: "Abril",
        5: "Maio", 
        6: "Junho", 
        7: "Julho", 
        8: "Agosto", 
        9: "Setembro", 
        10: "Outubro", 
        11: "Novembro", 
        12: "Dezembro"
    }
while True:
        try:
            numero = int(input("Informe o número do mês: ")) 
            if numero in meses:
                mes = meses[numero]
                print(f"O mês é: {mes}")
                break
            else:
                print("Erro: Digite um número entre 1 e 12!")      
        except ValueError:
            print("Erro: Digite um número inteiro válido!")