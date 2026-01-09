## Leitura Guiada U-Net

### **Introdução (Seção 1)**

Nesta seção, concentre-se em entender qual problema está sendo resolvido, as limitações das abordagens anteriores e a principal intuição (key insight) dos autores.

**Pontos de atenção:**

- Limitações do sliding-window: redundância e *trade-off* entre contexto e localização.
- Ideia central: rede totalmente convolucional com caminho expansivo simétrico e *skips* para recuperar detalhes finos.
- Objetivo: treinar *end-to-end* com poucos rótulos, usando forte augmentação.

**Questões que você deve responder:**

- Por que o sliding-window compromete velocidade e/ou precisão de bordas?
- Qual “insight” permite unir contexto amplo e detalhe fino na U-Net?
- Como a U-Net lida com a escassez de dados anotados?

### Arquitetura (Seção 2, Fig. 1)

**Pontos de atenção:**

- Caminho de contração: blocos *conv 3×3 + ReLU* (×2) → *max-pool 2×2*, dobrando canais a cada *downsample*.
- Caminho de expansão: *upsampling* → up-conv 2×2 (reduz canais pela metade) → concatenação com *feature maps* recortados do encoder → *conv 3×3 + ReLU* (×2).
- Conv válida (sem *padding*) → necessidade de recortes; atenção a tamanhos pares antes do *pooling*.
- Saída: *conv 1×1* para mapear 64 canais → *K* classes; 23 camadas conv no total.
- Overlap-tile (Fig. 2): segmentação de imagens arbitrariamente grandes com espelhamento nas bordas. 2015_-_U-Net_Convolutional_Netw…

**Questões que você deve responder:**

- Por que a U-Net prefere concatenação (e não soma) nas *skip connections*?
- O que obriga o recorte (*crop*) dos *feature maps* do encoder?
- Como a estratégia overlap-tile evita perda de contexto nos contornos?

### **Resultados (Seção 5)**

**Questões que você deve responder:**

- Onde a U-Net mais ganha sobre patch-based (métrica e motivo)?
- O que explica a diferença de desempenho entre PhC-U373 e DIC-HeLa?
- Além da acurácia, quais vantagens práticas a U-Net demonstra (tempo, dados, simplicidade de pipeline)?

### **Após a leitura**

- Contribuição central: arquitetura em “U”, skips com concatenação, overlap-tile, perda ponderada por pixel ou augmentation elástica? Justifique.
- Generalização: que adaptações fariam sentido para múltiplas escalas ou para classes muito desbalanceadas?
- Reprodutibilidade: como você organizaria um experimento moderno (PyTorch) que respeite os mesmos princípios de treino e perda?
- O que os autores querem dizer com "treinamento end-to-end, pixels-to-pixels"?  Por que isso foi um avanço tão significativo?