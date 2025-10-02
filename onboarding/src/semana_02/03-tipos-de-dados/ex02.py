""" Exercício 2 """

meses = ( "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho",     
        "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro" )

while True:
        try:
            numero = int(input("Informe o número do mês: ")) 
            if 1 <= numero <= 12:
                mes = meses[numero]
                print(f"O mês é: {mes}")
                break
            else:
                print("Erro: Digite um número entre 1 e 12!")      
        except ValueError:
            print("Erro: Digite um número inteiro válido!")