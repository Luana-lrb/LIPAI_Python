# Gráfico de barras
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/UFU/IC/onboarding/src/semana_4/classification_results_trial_0001.csv", sep=',')

# Personalizar
plt.figure(figsize=(5, 5))       
plt.title('Meu Título')            
plt.xlabel('Eixo X')               
plt.ylabel('Eixo Y')               
plt.legend(['Série 1'])           
plt.grid(True)  

# Exemplo de gráfico de barras
#plt.bar(['A', 'B'], [10, 15])
#plt.show()

# Histograma
#plt.hist(data['prob_benign'], bins=20)
#plt.show()

# Scatter plot - Dispersão
#plt.scatter(data['prob_malign'], data['prob_benign'], c=data['real_class'] == data['predicted_class'])

#cores = ['red''blue']
# Cores
#plt.scatter(data['prob_malign'], data['prob_benign'], c='red')             
#plt.scatter(data['prob_malign'], data['prob_benign'], c='red', alpha=0.7)  # alpha é para transparência

# Marcadores
#plt.scatter(data['prob_malign'], data['prob_benign'], marker='x')      # x, o, +, ., etc
#plt.scatter(data['prob_malign'], data['prob_benign'], s=100)           # Tamanho dos pontos
#plt.show()

# Gráfico de pizza
#plt.pie([30, 70], labels=['A', 'B'])
#plt.show()

# Gráfico de linha
#plt.plot(data['prob_malign'], data['prob_benign'])
#plt.show()

# Subplots
#fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
#ax1.bar(['A', 'B'], [1, 2])
#ax2.scatter('prob_malign', 'prob_benign', data=data, c='real_class', cmap='viridis')
#plt.show()

#plt.axhline(y=0.5, color='gray', linestyle='--')  # Linha horizontal
#plt.axvline(x=0.5, color='gray', linestyle='--')  # Linha vertical

# Exemplos
data['real_class'].value_counts().plot(kind='bar')
plt.title('Distribuição por classe Real')
plt.show()


