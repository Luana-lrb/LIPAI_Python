## Leitura Guiada FCN

### **Introdução (Seção 1)**

Nesta seção, concentre-se em entender qual problema está sendo resolvido, as limitações das abordagens anteriores e a principal intuição (key insight) dos autores.

**Pontos de atenção:**

- A tensão inerente entre semântica ("o quê") e localização ("onde") na segmentação.
- A ideia central de construir redes "totalmente convolucionais" (FCNs) que podem processar entradas de qualquer tamanho.
- A proposta de adaptar redes de classificação (como AlexNet, VGG) para segmentação.
- A introdução da arquitetura que combina camadas profundas (grosseiras) e rasas (finas).
**Questões que você deve responder:**

- Qual é a principal limitação das CNNs de classificação (como a VGG) quando aplicadas a tarefas de predição densa (pixel a pixel)?
- Qual é a "intuição chave" (key insight) que os autores propõem para superar essa limitação?
- Como os autores propõem resolver a tensão entre a informação semântica (global) e a informação de aparência (local)?

### **Redes Totalmente Convolucionais (Seção 3)**

**Pontos de atenção:**

- O processo de "convolucionalização", tratando camadas *fully connected* (FC) como convoluções 1x1.
- A vantagem de eficiência dessa abordagem sobre a avaliação *patch-by-patch* (pedaço por pedaço).
- A necessidade de *upsampling* (amostragem para cima) para recuperar a resolução original.
- 
- A ideia de usar "convolução transposta" (*backwards convolution* ou *deconvolution*) como uma camada de *upsampling* que pode ser aprendida.
- A discussão sobre treinamento *patchwise* vs. *whole image* (imagem inteira)

**Questões que você deve responder:**

- Como exatamente os autores convertem uma camada *fully connected* (totalmente conectada) em uma camada convolucional?
- Qual é o problema da saída de uma rede "convolucionalizada" (como descrito na Seção 3.1) e por que o *upsampling* é necessário?
- O que é a "convolução transposta" (ou deconvulução) e por que ela é preferível a uma interpolação simples (como a bilinear)?
- 
- Por que os autores argumentam que treinar com a imagem inteira é mais eficiente que o treinamento com *patches*?

### **Arquitetura de Segmentação (Seção 4)**

**Pontos de atenção:**

- A FCN "base" (como a FCN-VGG16), que é simplesmente a rede VGG com *fine-tuning* e uma camada de *upsampling* no final (depois chamada de FCN-32s).
- O problema de "saída grosseira" (coarse output) da FCN-32s.
- A introdução das **skip connections** (conexões de salto) para fundir predições de camadas em diferentes resoluções.
- A lógica por trás da FCN-16s (fusão com pool4) e da FCN-8s (fusão com pool3). (Veja a Figura 3 para um diagrama claro ).
**Questões que você deve responder:**

- Qual é a arquitetura da FCN-32s? Por que sua saída, mesmo após o *upsampling*, é considerada "insatisfatoriamente grosseira"?
- Como a FCN-16s melhora a FCN-32s? Qual informação da rede ela está "resgatando"?
- Explique a arquitetura da FCN-8s. Como ela combina informações de três escalas diferentes?

### **Resultados (Seção 5)**

Observe como os resultados são apresentados e a comparação com o estado-da-arte da época.

**Pontos de atenção:**

- A métrica principal: *mean Intersection over Union* (mIU).
- A comparação de desempenho no PASCAL VOC 2011/2012 contra o método SDS (que era o estado-da-arte).
- A melhoria de desempenho ao mover de FCN-32s para FCN-16s e FCN-8s (Tabela 2).
- A enorme vantagem em velocidade de inferência.

**Questões que você deve responder:**

- Quais foram os ganhos (em mIU) obtidos no PASCAL VOC 2012 em comparação com o método SDS?
- Qual foi o impacto das *skip connections* no desempenho (comparando FCN-32s, FCN-16s e FCN-8s na Tabela 2)?
- Além da precisão, qual outra grande vantagem a FCN demonstrou ter sobre os métodos concorrentes?

### **Após a leitura**

- Qual você considera ser a principal contribuição deste artigo: a "convolucionalização" (Seção 3.1), o *upsampling* aprendível (Seção 3.3) ou as *skip connections* (Seção 4.2)?
- O que os autores querem dizer com "treinamento end-to-end, pixels-to-pixels"?  Por que isso foi um avanço tão significativo?