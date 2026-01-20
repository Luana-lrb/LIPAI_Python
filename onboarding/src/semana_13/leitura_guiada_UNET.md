## Leitura Guiada U-Net

### **Introdução (Seção 1)**

Nesta seção, concentre-se em entender qual problema está sendo resolvido, as limitações das abordagens anteriores e a principal intuição (key insight) dos autores.

**Pontos de atenção:**

- Limitações do sliding-window: redundância e *trade-off* entre contexto e localização.
- Ideia central: rede totalmente convolucional com caminho expansivo simétrico e *skips* para recuperar detalhes finos.
- Objetivo: treinar *end-to-end* com poucos rótulos, usando forte augmentação.

**Questões que você deve responder:**

- Por que o sliding-window compromete velocidade e/ou precisão de bordas?
>No paper explica que é lento porque precisa processar cada patch separadamente com muita redundância, e há um trade-off entre precisão de localização e uso de contexto - patches grandes precisam de mais max-pooling (reduz precisão), patches pequenos veem pouco contexto.

>"First, it is quite slow because the network must be run separately for each patch, and there is a lot of redundancy due to overlapping patches. Secondly, there is a trade-off between localization accuracy and the use of context. .Larger patches require more max-pooling layers that reduce the localization accuracy, while small patches allow the network to see only little context." 
- Qual “insight” permite unir contexto amplo e detalhe fino na U-Net?
>A ideia é usar camadas de upsampling (ao invés de pooling) e combinar features de alta resolução do caminho de contração com a saída upsampled. Isso permite localização precisa mantendo contexto.

>"The main idea in[9] is to supplement a usual contracting network by successive layers,where pooling operators are replaced by upsampling operators."

- Como a U-Net lida com a escassez de dados anotados?
>Usa data augmentation excessiva, especialmente deformações elásticas, permitindo que a rede aprenda invariância sem precisar ver essas transformações nos dados anotados.

>"As for our tasks there is very little training data available, we use excessive data augmentation by applying elastic deformations to the available training images."

### Arquitetura (Seção 2, Fig. 1)

**Pontos de atenção:**

- Caminho de contração: blocos *conv 3×3 + ReLU* (×2) → *max-pool 2×2*, dobrando canais a cada *downsample*.
- Caminho de expansão: *upsampling* → up-conv 2×2 (reduz canais pela metade) → concatenação com *feature maps* recortados do encoder → *conv 3×3 + ReLU* (×2).
- Conv válida (sem *padding*) → necessidade de recortes; atenção a tamanhos pares antes do *pooling*.
- Saída: *conv 1×1* para mapear 64 canais → *K* classes; 23 camadas conv no total.
- Overlap-tile (Fig. 2): segmentação de imagens arbitrariamente grandes com espelhamento nas bordas. 2015_-_U-Net_Convolutional_Netw…

**Questões que você deve responder:**

- Por que a U-Net prefere concatenação (e não soma) nas *skip connections*?
> No upsampling há "a large number of feature channels, which allow the network to propagate context information to higher resolution layers". A concatenação preserva TODOS os canais (contexto e detalhes), enquanto soma misturaria a informação.

- O que obriga o recorte (*crop*) dos *feature maps* do encoder? 
> "The cropping is necessary due to the loss of border pixels in every convolution" 

> Como usam "valid convolutions" (sem padding), cada conv 3×3 reduz a imagem em 2 pixels (1 de cada lado). Isso acumula ao longo da rede.

- Como a estratégia overlap-tile evita perda de contexto nos contornos?
> Exemplificado na figura 2 do paper, para segmentar a área amarela, usa dados da área azul (maior) como entrada. Nas bordas onde falta contexto, espelha a imagem.

> "To predict the pixels in the border region of the image, the missing context is extrapolated by mirroring the input image"


### **Resultados (Seção 4)**

**Questões que você deve responder:**

- Onde a U-Net mais ganha sobre patch-based (métrica e motivo)?
> U-Net ganha tempo ao processar imagem inteira de uma vez, enquanto sliding-window é lento e redundante. Na tabela 1 do paper, Warping error: 0.0003529 (U-Net) vs 0.000420 (IDSIA/Ciresan) e o Rand error: 0.0382 vs 0.0504.


- O que explica a diferença de desempenho entre PhC-U373 e DIC-HeLa? 
> Na tabela 2 do paper, PhC-U373: 92% IOU (35 imagens treino), DIC-HeLa: 77.5% IOU (20 imagens treino). O que pode explicar é que tem menos dados de treino no DIC-HeLa, além do DIC ser mais desafiador por ter células mais próximas e menor contraste.

- Além da acurácia, quais vantagens práticas a U-Net demonstra (tempo, dados, simplicidade de pipeline)?
> Velocidade: "less than a second" para imagem 512×512
> Tempo treino: "only 10 hours on a NVidia Titan GPU"
> Dados: "trained end-to-end from very few images"

### **Após a leitura**

- Contribuição central: arquitetura em “U”, skips com concatenação, overlap-tile, perda ponderada por pixel ou augmentation elástica? Justifique.

> A arquitetura em U com skip connections por concatenação é a contribuição mais citada no paper.

- Generalização: que adaptações fariam sentido para múltiplas escalas ou para classes muito desbalanceadas?

> A U-Net já captura múltiplas escalas através dos níveis de pooling (de 572×572 até 28×28), mas apenas sequencialmente. Para múltiplas escalas poderia fazer concatenações densas (conectar cada nível do encoder a múltiplos níveis do decoder). Para classes muito desbalanceadas usa peso w(x) = wc(x) + w0·exp(...) onde: wc(x) = peso para balancear frequência de classes.

- Reprodutibilidade: como você organizaria um experimento moderno (PyTorch) que respeite os mesmos princípios de treino e perda?
> Para reproduzir, mantar a arquitetura exata (23 camadas conv, concatenação), loss ponderada, augmentation elástica agressiva, batch=1, momentum=0.99, e implementar overlap-tile para imagens grandes.

- O que os autores querem dizer com "treinamento end-to-end, pixels-to-pixels"?  Por que isso foi um avanço tão significativo? 
> Ao contrário do sliding-window que classifica patches individualmente, a U-Net mapeia imagem completa, segmentação completa em uma única passada forward, sem pós-processamento. Foi um avanço significativo pelo impacto no tempo de execução.