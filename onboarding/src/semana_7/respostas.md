## **Questões Respondidas** 

<h2>Redes Neurais Artificiais e PyTorch</h2>


**1 - Com base no material apresentado no notebook, o que é uma função de ativação (como a ReLU)? Por que normalmente usamos entre as camadas?**

*O que é uma função de ativação:*

Uma função de ativação é um componente fundamental dos neurônios artificiais que processa a combinação linear entre os inputs (entradas) e os pesos sinápticos, transformando essa soma ponderada em um sinal de saída(mais o bias). Ela determina se e como um neurônio deve ser "ativado" com base nas informações que recebe.
Assim sendo, Matematicamente, se temos inputs x₁, x₂, ..., xₙ com pesos w₁, w₂, ..., wₙ e bias b, a função de ativação **f** processa: **Saída = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)**

A ReLU (Rectified Linear Unit) é uma das funções de ativação mais populares, definida como:

ReLU(x) = max(0, x)
Se x > 0, retorna x
Se x ≤ 0, retorna 0

*Por que usamos funções de ativação entre camadas:*

Porque ela introduz a não-linearidade, aumenta a capacidade de aproximação universal de qualquer função contínua, permitem
um controle do fluxo de informação, atuam como "filtros", permitindo que apenas certas informações passem para as próximas camadas (no caso da ReLU, apenas valores positivos).
Além de darem mais estabilidade no treinamento e aumentarem a eficiência computacional. Ou seja, sem essas funções de ativação não-lineares entre as camadas, mesmo uma rede com milhões de parâmetros seria limitada a aprender apenas relações lineares, perdendo toda a capacidade de modelar a complexidade do mundo real.

**2 -  Explique o que cada uma das seguintes linhas de código faz e por que ela é necessária:**
**a. model.train()**
Define o modelo para o modo de treinamento, ativa comportamentos específicos necessários durante o treinamento e habilita dropout, batch normalization e outras camadas que se comportam diferentemente durante treino e durante a inferência. Permitindo que os pesos sinápticos e os bias dos neurônios adaptáveis sejam atualizados na retro-propagação. É necessária, porque algumas camadas têm comportamentos distintos entre treinamento e inferência, como no dropout, que urante treino, "desliga" neurônios aleatoriamente para regularização; e que durante inferência, mantém todos ativos; como na batch normalization, que durante treino, usa estatísticas do batch atual; e que durante inferência, usa estatísticas aprendidas; e como nas camadas recorrentes, que podem ter diferentes comportamentos de memória

**b. optimizer.step()** 
Efetivamente atualiza os parâmetros (pesos e bias) do modelo baseado nos gradientes calculados e aplica o algoritmo de otimização escolhido (SGD, Adam, etc.) Portanto, "Aprende" ajustando os pesos na direção que reduz a loss function. É necessária porque, sem esta linha, os gradientes seriam calculados mas os parâmetros nunca seriam atualizados e o modelo não aprenderia nada.

**c. Qual a diferença fundamental entre os modos model.train() e model.eval()?**

O propósito do model.train() é preparar para treinamento, enquanto o do model.eval() é preparar para inferência/avaliação. O dropout do model.train() é ativo (desliga neurônios), enquanto o do model.eval() é inativo (todos neurônios ativos). A Batch Normalizationdo model.train() usa estatísticas do batch atual + atualiza running stats, enquanto a do model.eval() é usa running statistics fixas.Os Gradientes do model.train()são habilitados por padrão, enquanto os do model.eval() são geralmente usados com torch.no_grad().Além disso tudo, o comportamento do model.train()é estocástico, enquanto o do model.eval() é determinístico. 
Essa distinção é crucial porque, garante reprodutibilidade durante inferência, evita vazamento de informações de teste durante avaliação, otimiza performance (eval é mais rápido) e previne overfitting através da regularização adequada durante treino.

**Demais questões foram respondidas nos codigo_3.ipynb, codigo_4.ipynb e codigo_5.ipynb**
